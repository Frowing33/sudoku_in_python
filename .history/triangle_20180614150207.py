import math

x1 = 1
y1 = 2

x2 = -1
y2 = 6

x3 = 3
y3 = 4

def distance(x1,y1, x2, y2):
    lenght = math.sqrt( (x1-x1)**1  + (y1-y2)**2)
    return lenght

print("dlugosc AB = ", distance(x1, x2, y1, y2) )
print("dlugosc BC = ", distance(x2, x3, y2, y3) )
print("dlugosc AC = ", distance(x1, x3, y1, y3) )