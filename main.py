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

def main():
    image  = Image(320, 200)
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.5, Material(Color.from_hex("#FF0000"))),
               Sphere(Point(-.75, 0, 0), 0.2, Material(Color.from_hex("#00FF00")))]
    lights = [Light(Point(1.5, -.5, -10.0), Color.from_hex('#FFFFFF')),
              Light(Point(-1.5, .5, -10.0), Color.from_hex('#00FFFF'))]
    scene = Scene(camera, objects, lights, 320, 200)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()