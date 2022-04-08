import math
from turtle import circle
class Circle:
    def __init__(self, _radius):
        self.radius = _radius

    def calculate_area(self):
        return (math.pi * (self.radius ** 2))

    def __repr__(self):
         rep = 'circle(radius: ' + str(self.radius) + ', area: ' + str(self.calculate_area()) + ')'
         return rep

    def __add__(self, other):
        return Circle((self.radius + other.radius))

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius   

    def __eq__(self, other): 
        return self.radius == other.radius        


c = Circle(6)
c2 = Circle(3)
print(repr(c))
print(repr(c + c2))
print(c < c2)
print(c > c2)
print(c == c2)

c3 = Circle(10)
circles = [c, c2, c3, c +c3, c + c2]

print(circles)
circles.sort()
print(circles)
