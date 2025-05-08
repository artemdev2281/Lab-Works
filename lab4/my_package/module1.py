class vector:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.coord = (x1 - x2, y1 - y2, z1 - z2)
        self.len = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2) ** 2)**0.5
    def info(self):
        print(f'The coordinates of your vector are {self.coord} and len is {self.len}')