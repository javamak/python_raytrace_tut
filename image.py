class Image:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.pixels = [[None for _ in range(w)] for _ in range(h)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, img_file):
        Image.write_ppm_header(img_file,  self.h, self.w)
        self.write_ppm_raw(img_file)

    @staticmethod
    def write_ppm_header(img_file, width=None, height=None):
        img_file.write("P3 {} {}\n255\n".format(width, height))

    def write_ppm_raw(self, img_file):
        def to_byte(x):
            return round(max(min(x * 255, 255), 0))

        for row in self.pixels:
            for color in row:
                img_file.write("{} {} {} ".format(to_byte(color.r), to_byte(color.g), to_byte(color.b)))
            img_file.write('\n')
