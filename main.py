#!/usr/bin/evn python


from image import Image
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material
from scene_loader import load_scene

def main():

    """camera = Vector(0, -0.35, -1)
    objects = [Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
               Sphere(Point(0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980"))),
               Sphere(Point(0, 10000.5, 1), 10000.0, Material(Color.from_hex("#803980"), ambient=0.2, specular=0.2))]
    lights = [Light(Point(1.5, -.5, -10.0), Color.from_hex('#FFFFFF')),
              Light(Point(-0.5, -10.5, 0.0), Color.from_hex('E6E6E6'))]
    scene = Scene(camera, objects, lights, 320, 200)"""

    scene = load_scene('./scenes/2balls.json')
    engine = RenderEngine()
    image = engine.render(scene)

    with open("2balls.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()