class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

krug = Circle(6)
print(krug.get_radius())
print(krug.set_radius(12))