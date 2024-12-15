class equation:
    def __init__(self, a, b, c):
        self.d = b**2 - 4*a*c
        self.x1 = -b + self.d**0.5
        self.x2 = -b - self.d**0.5
    def decision(self):
        if self.d > 0:
            print(f'x1 = {self.x1}, x2 = {self.x2}')
        elif self.d == 0:
            print(f'x = {self.x1}')
        else:
            print(f'There are no solutions')