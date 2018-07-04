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

ab = distance(x1, y1, x2, y2)
bc = distance(x2, y2, x3, y3)
ac = distance(x1, y1, x3, y3)

print("dlugosc AB = ",ab  )
print("dlugosc BC = ",bc  )
print("dlugosc AC = ",ac  )

p = float((ab + bc + ac)/2)
#area = 
print("Area of triangle is: ", math.sqrt(p*(p-ab)*(p-bc)*(p-ac)))