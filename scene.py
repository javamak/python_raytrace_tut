from vector import Vector
from sphere import Sphere
from light import Light
from material import Material, ChequeredMaterial
from color import Color
from point import Point


class Scene:
    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height

    def __init__(self, d):
        self.camera = Vector(**d['camera'])
        self.objects = []
        self.lights = []
        for obj in d['objects']:
            mat = self.create_material(obj)
            point = Point(**obj['center'])
            self.objects.append(Sphere(point, obj['radius'], mat))

        for obj in d['lights']:
            col = obj['color']
            col = Color.from_hex(col)
            self.lights.append(Light(Point(**obj['position']), col))

        self.width = d['width']
        self.height = d['height']

    def create_material(self, obj):
        if 'chequered_material' in obj:
            mat = obj['chequered_material']
            col1 = Color.from_hex(mat['color1'])
            del (mat['color1'])
            col2 = Color.from_hex(mat['color2'])
            del (mat['color2'])
            mat = ChequeredMaterial(color1=col1, color2=col2, **mat)
        else:
            mat = obj['material']
            col = Color.from_hex(mat['color'])
            del (mat['color'])
            mat = Material(color=col, **mat)
        return mat

    def __str__(self):
        return "camera.x:{}, camera.y:{}".format(self.camera.x, self.camera.y)
