

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

s = Circle (5)
print("圆的面积是:", s.area())