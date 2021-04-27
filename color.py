
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        return Color(self.r+other.r, self.g+other.g, self.b+other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __mul__(self, other):
        assert not isinstance(other, Color)
        return Color(self.r * other, self.g * other, self.b * other)

    def __rmul__(self, other):
        return self * other

    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        x = int(hexcolor[1:3], 16) / 255
        y = int(hexcolor[3:5], 16) / 255
        z = int(hexcolor[5:], 16) / 255
        return Color(x, y, z)

