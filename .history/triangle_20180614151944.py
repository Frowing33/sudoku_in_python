import math
tri1 = [0, 0,  0, 3, 5, 0]
tri2 = [0, 0,  2, 2, 4, 0]
tri3 = [1, 2, -1, 6, 3, 5]

x1 = tri1[0]
y1 = tri1[1]
x2 = tri1[2]
y2 = tri1[3]
x3 = tri1[4]
y3 = tri1[5]


def distance(a1, b1, a2, b2):
    lenght = math.sqrt( (a1-a2)**2  + (b1-b2)**2 )
    return lenght
print("dlugosc ffds = ", math.sqrt( (0-0)**2  + (0-3)**2 ) )
print(x1, y1, x2, y2 )
print("dlugosc AB = ", distance(x1, y1, x2, y2) )
print("dlugosc BC = ", distance(x2, y2, x3, y3) )
print("dlugosc AC = ", distance(x1, y1, x3, y3) )