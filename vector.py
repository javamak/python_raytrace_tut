import math

class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x*other, self.y*other, self.z*other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x/other, self.y/other, self.z/other)

    def __rtruediv__(self, other):
        return self / other

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        return self/self.magnitude()

    def dot_product(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z

    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z