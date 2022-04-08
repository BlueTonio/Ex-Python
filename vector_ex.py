from cmath import sqrt
from re import X


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z 

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __mul__(self, other):
         return(self.x * other.x) + (self.y * other.y) + (self.z * other.z)
             
    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return Vector(self.x == other.x, self.y == other.y, self.z == other.z)

    def __repr__(self):
        rep = 'vector(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) +')'
        return rep    


                   
   
v = Vector(5,6,8)
print(v + Vector(7,9,10))
print(v * Vector(7,9,10))
print(v == Vector(7,9,10))
print(repr(v)) 