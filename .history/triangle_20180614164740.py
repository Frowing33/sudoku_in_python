import math
tri1 = [0, 0,  0, 3, 5, 0]
tri2 = [0, 0,  2, 2, 4, 0]
tri3 = [1, 2, -1, 6, 3, 5]
def inputVertices():
    test = True
    while test:
        try:
            numbers = [int(x) for x in input('Input numbers to sort: ').split()]  
            test = False
            return numbers  
        except ValueError: 
            print("Please enter ONLY a numbers separeted with space!")
            continue

triangle = inputVertices()
print("Triangle Vertices:" , triangle)
x1 = triangle[1]
y1 = triangle[2]
x2 = triangle[3]
y2 = triangle[4]
x3 = triangle[5]
y3 = triangle[6]

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
print("Area of triangle is: ", round( math.sqrt(p*(p-ab)*(p-bc)*(p-ac)), 2) )