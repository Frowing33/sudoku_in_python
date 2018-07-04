import math
tri1 = [0, 0,  0, 3, 5, 0]
tri2 = [0, 0,  2, 2, 4, 0]
tri3 = [1, 2, -1, 6, 3, 5]
def inputVertices():
    test = True
    while test:
        try:
            numbers = [int(x) for x in input('Input triangle Vertiecs: ').split()]  
            if len(numbers) < 6:
                print("Input all 6 vertices: ")
                continue
            elif len(numbers) > 6:
                print("Input ONLY 6 vertices: ")
                continue
            test = False
            return numbers  
        except ValueError: 
            print("Please enter ONLY a numbers separeted with space!")
            continue

triangle = inputVertices()
print("Triangle Vertices:" , triangle)
x1 = triangle[0]
y1 = triangle[1]
x2 = triangle[2]
y2 = triangle[3]
x3 = triangle[4]
y3 = triangle[5]

def distance(a1, b1, a2, b2):
    lenght = math.sqrt( (a1-a2)**2  + (b1-b2)**2 )
    return lenght

ab = distance(x1, y1, x2, y2)
bc = distance(x2, y2, x3, y3)
ac = distance(x1, y1, x3, y3)

print(" Lenght AB = ",ab  )
print(" Lenght BC = ",bc  )
print(" Lenght AC = ",ac  )

p = float((ab + bc + ac)/2)
print("Area of triangle is: ", round( math.sqrt(p*(p-ab)*(p-bc)*(p-ac)), 2) )