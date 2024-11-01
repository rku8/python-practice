from array import array

values = array('i', [1, 2, 3, 4, 5, 6])
# print(values[3])

import math

# print(math.log(22026.465794806718))

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        

vec = Vector(2, 5)
vec2 = Vector(2.0, 5)
print(vec == vec2)
        
