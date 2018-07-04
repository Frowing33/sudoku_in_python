row1 = [0,0,0,0,0,0,0,0,0]
row2 = [0,0,0,5,0,6,0,0,0] 
row3 = [0,0,1,0,0,0,0,3,0] 

row4 = [0,9,5,0,0,0,2,0,0] 
row5 = [0,0,0,0,0,1,6,0,7] 
row6 = [1,0,6,0,0,9,0,0,5] 

row7 = [7,0,0,8,0,3,9,0,0] 
row8 = [0,3,8,9,0,0,0,2,0] 
row9 = [0,5,0,0,2,0,7,0,0] 

#for i in row1:
#    print(i)
#print(list[1][2])

print(row1)
print(row2)
print(row3)
print("")
print(row4)
print(row5)
print(row6)
print("")
print(row7)
print(row8)
print(row9)

#num1 = int(input("Enter a number (or a letter to exit) "))
x = input("Wprowadz x y z:") 


if int(x[0])==1:
    row1[int(x[2])-1]=x[4]
    print("ok")

print(x[0])
print(x[2])
print(x[4])


print(row1)

#elif x[0]==2:
 #   row2[x[2]]=x[4]
#elif x[0]==3:
#    row3[x[2]]=x[4]
    




#print(new)
#rds.insert(index, "is")