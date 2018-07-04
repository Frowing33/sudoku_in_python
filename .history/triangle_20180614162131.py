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

print("dlugosc AB = ", math.sqrt( (0-0)**2  + (0-3)**2 ) )
print(x1, y1, x2, y2 )
print("dlugosc BC = ", math.sqrt( (0-5)**2  + (3-0)**2 ) )
print(x2, y2, x3, y3 )
print("dlugosc AC = ", math.sqrt( (0-5)**2  + (0-0)**2 ) )
print(x1, y1, x3, y3 )

ab = distance(x1, y1, x2, y2)
bc = distance(x2, y2, x3, y3)
ac = distance(x1, y1, x3, y3)

print("dlugosc AB = ",ab  )
print("dlugosc BC = ",bc  )
print("dlugosc AC = ",ac  )

p = float((ab + bc + ac)/2)
print("p = ", p)
area = math.sqrt(p(p-ab)*(p-bc)*(p-ac))
print("Area of triangle is: ", area)