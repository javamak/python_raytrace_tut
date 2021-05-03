#!/usr/bin/evn python

from engine import RenderEngine
from scene_loader import load_scene
import time

def main():

    """camera = Vector(0, -0.35, -1)
    objects = [Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
               Sphere(Point(0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980"))),
               Sphere(Point(0, 10000.5, 1), 10000.0, Material(Color.from_hex("#803980"), ambient=0.2, specular=0.2))]
    lights = [Light(Point(1.5, -.5, -10.0), Color.from_hex('#FFFFFF')),
              Light(Point(-0.5, -10.5, 0.0), Color.from_hex('E6E6E6'))]
    scene = Scene(camera, objects, lights, 320, 200)"""

    start_time = time.time()
    scene = load_scene('./scenes/2balls.json')
    engine = RenderEngine()
    image = engine.render(scene)

    with open("2balls.ppm", "w") as img_file:
        image.write_ppm(img_file)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()