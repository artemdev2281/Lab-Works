class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return f'radius = {self.radius}'
    def set_radius(self, new_radius):
        self.radius = new_radius
        return f'new radius = {self.radius}'
r = Circle(10)
print(r.get_radius())
print(r.set_radius(11))
print(r.get_radius())