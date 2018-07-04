import math

x1 = 1
y1 = 2

x2 = -1
y2 = 6

x3 = 3
y3 = 5

def distance(a1,b1, a2, b2):
    lenght = math.sqrt( (a1-a1)**1  + (b1-b2)**2)
    return lenght

print("dlugosc AB = ", distance(x1, x2, y1, y2) )
print("dlugosc BC = ", distance(x2, x3, y2, y3) )
print("dlugosc AC = ", distance(x1, x3, y1, y3) )