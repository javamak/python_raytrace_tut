from image import Image
from ray import Ray
from point import Point
from color import Color
from multiprocessing import Value, Process
import tempfile
import shutil
from pathlib import Path


class RenderEngine:
    def __init__(self):
        self.MIN_DISPLACE = 0.001
        self.MAX_DEPTH = 5

    def render(self, scene, hmin, hmax, part_file, rows_done):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = 1.0
        xstep = (x1 - x0) / (width - 1)

        y0 = -1.0 / aspect_ratio
        y1 = 1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        image = Image(width, hmax - hmin)

        for j in range(hmin, hmax):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                ray = Ray(camera, Point(x, y) - camera)
                image.set_pixel(i, j - hmin, self.ray_trace(ray, scene))

            # update progress
            if rows_done:
                with rows_done.get_lock():
                    rows_done.value += 1
                    print("{:3.0f}%".format(float(rows_done.value) / float(height) * 100), end="\r")

        with open(part_file, "w") as part_file:
            image.write_ppm_raw(part_file)

    def ray_trace(self, ray, scene, depth=0):
        color = Color(0, 0, 0)
        # find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if not obj_hit:
            return color

        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)

        if depth < self.MAX_DEPTH:
            new_ray_pos = hit_pos + hit_normal * self.MIN_DISPLACE
            new_ray_dir = ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            new_ray = Ray(new_ray_pos, new_ray_dir)
            # Attenuate the reflected ray found by reflection coefficient
            color += self.ray_trace(new_ray, scene, depth + 1) * obj_hit.material.reflection

        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None

        for obj in scene.objects:
            dist = obj.intesects(ray)
            if dist and (not obj_hit or dist < dist_min):
                dist_min = dist
                obj_hit = obj

        return dist_min, obj_hit

    def color_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.material
        obj_color = material.color_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_hex(("#FFFFFF"))
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # diffuse shading (Lambert)
            color += obj_color * material.diffuse * max(normal.dot_product(to_light.direction), 0)

        # specualar shadding (Blinn-Phong)
        half_vector = (to_light.direction + to_cam).normalize()
        color += light.color * material.specular * max(normal.dot_product(half_vector), 0) ** specular_k

        return color

    def render_multiprocess(self, scene, process_count, file_obj):
        def split_range(count, parts):
            d, r = divmod(count, parts)
            return [(i * d + min(i, r), (i + 1) * d + min(i + 1, r)) for i in range(parts)]

        width = scene.width
        height = scene.height
        ranges = split_range(height, process_count)
        print(ranges)
        temp_dir = Path(tempfile.mkdtemp())
        temp_file_tmpl = "part_{}.ppm"
        processes = []
        try:
            rows_done = Value("i", 0)
            for hmin, hmax in ranges:
                part_file = temp_dir / temp_file_tmpl.format(hmin)
                processes.append(Process(target=self.render, args=(scene, hmin, hmax, part_file, rows_done)))

            for process in processes:
                process.start()

            for process in processes:
                process.join()

            # reconstruct the image
            Image.write_ppm_header(file_obj, width, height)
            for hmin, _ in ranges:
                part_file = temp_dir / temp_file_tmpl.format(hmin)
                file_obj.write(open(part_file, "r").read())
        finally:
            print(temp_dir)
            shutil.rmtree(temp_dir)

