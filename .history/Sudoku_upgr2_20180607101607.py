#row1 = [0,0,0,0,0,0,0,0,0]
#row2 = [0,0,0,5,0,6,0,0,0] 
#row3 = [0,0,1,0,0,0,0,3,0] 

#row4 = [0,9,5,0,0,0,2,0,0] 
#row5 = [0,0,0,0,0,1,6,0,7] 
#row6 = [1,0,6,0,0,9,0,0,5] 

#row7 = [7,0,0,8,0,3,9,0,0] 
#row8 = [0,3,8,9,0,0,0,2,0] 
#row9 = [0,5,0,0,2,0,7,0,0] 

columns = [1,2,3,4,5,6,7,8,9]
row1 = [9,8,7,4,3,2,5,6,1]
row2 = [2,4,3,5,1,6,8,7,9] 
row3 = [5,6,1,7,9,8,4,3,2] 

row4 = [3,9,5,6,4,7,2,1,8] 
row5 = [8,2,4,3,5,1,6,9,7] 
row6 = [1,7,6,2,8,9,3,4,5] 

row7 = [7,1,2,8,6,3,9,5,4] 
row8 = [4,3,8,9,7,5,1,2,6] 
row9 = [0,5,0,0,2,0,7,0,0] 

def print_sudoku():
    print('   ', columns[0],columns[1],columns[2], sep='  ', end="     ")
    print(columns[3],columns[4],columns[5], sep='  ', end="     ")
    print(columns[6],columns[7],columns[8], sep='  ')

    print("  -----------------------------------" )
    


    print('1 |', row1[0],row1[1],row1[2], sep='  ', end="  |  ")
    print(row1[3],row1[4],row1[5], sep='  ', end="  -  ")
    print(row1[6],row1[7],row1[8], sep='  ')

    print('2 |', row2[0],row2[1],row2[2], sep='  ', end="  |  ")
    print(row2[3],row2[4],row2[5], sep='  ', end="  -  ")
    print(row2[6],row2[7],row2[8], sep='  ')

    print('3 |', row3[0],row3[1],row3[2], sep='  ', end="  |  ")
    print(row3[3],row3[4],row3[5], sep='  ', end="  -  ")
    print(row3[6],row3[7],row3[8], sep='  ')

    print("  -----------------------------------" )

    print('4 |', row4[0],row4[1],row4[2], sep='  ', end="  |  ")
    print(row4[3],row4[4],row4[5], sep='  ', end="  -  ")
    print(row4[6],row4[7],row4[8], sep='  ')

    print('5 |', row5[0],row5[1],row5[2], sep='  ', end="  |  ")
    print(row5[3],row5[4],row5[5], sep='  ', end="  -  ")
    print(row5[6],row5[7],row5[8], sep='  ')

    print('6 |', row6[0],row6[1],row6[2], sep='  ', end="  |  ")
    print(row6[3],row6[4],row6[5], sep='  ', end="  -  ")
    print(row6[6],row6[7],row6[8], sep='  ')
    print("")
    print('7 |', row7[0],row7[1],row7[2], sep='  ', end="  |  ")
    print(row7[3],row7[4],row7[5], sep='  ', end="  -  ")
    print(row7[6],row7[7],row7[8], sep='  ')

    print('8 |', row8[0],row8[1],row8[2], sep='  ', end="  |  ")
    print(row8[3],row8[4],row8[5], sep='  ', end="  -  ")
    print(row8[6],row8[7],row8[8], sep='  ')

    print('9 |', row9[0],row9[1],row9[2], sep='  ', end="  |  ")
    print(row9[3],row9[4],row9[5], sep='  ', end="  -  ")
    print(row9[6],row9[7],row9[8], sep='  ')
    print("")
print("Your sudoku to solve:")
print_sudoku()
'''
def strings_to_ints(rowx):
    for item in rowx:
        if isinstance(item,str):
            item=int(item)
'''
solve_checker=False

while solve_checker==False:
    print("Wprowadź 3 liczby w formacie x y z, gdzie:")
    print("Pierwsza liczba to współrzędna pionowa")
    print("Druga liczba to współrzędna pozioma")
    print("Trzecia liczba to liczba, którą wpisujesz (liczby oddzielaj spacjami) ")
    x = input("Wprowadź x y z:")

    numbers= "0123456789"
    if len(x) != 5: #and str(x[0]) not in numbers and str(x[2]) not in numbers and str(x[5]) not in numbers:
        print("BŁĄD - niepoprawny format!\n ")
        continue

    if (str(x[0]) not in numbers) or (str(x[2]) not in numbers) or (str(x[4]) not in numbers) or (str(x[1]) != " "):
            print("BŁĄD - niepoprawny format!\n ")
            continue 
    else:
            print(" Wprowadzono poprawne dane! ")

    if int(x[0])==1:
        row1[int(x[2])-1]=int(x[4])
    elif int(x[0])==2:
        row2[int(x[2])-1]=int(x[4])
    elif int(x[0])==3:
        row3[int(x[2])-1]=int(x[4])
    elif int(x[0])==4:
        row4[int(x[2])-1]=int(x[4])
    elif int(x[0])==5:
        row5[int(x[2])-1]=int(x[4])
    elif int(x[0])==6:
        row6[int(x[2])-1]=int(x[4])
    elif int(x[0])==7:
        row7[int(x[2])-1]=int(x[4])
    elif int(x[0])==8:
        row8[int(x[2])-1]=int(x[4])
    elif int(x[0])==9:
        row9[int(x[2])-1]=int(x[4])

    print_sudoku()

    if sum(row1) == 45 and sum(row2) == 45 and sum(row3) == 45 and sum(row4) == 45 and sum(row5) == 45 and sum(row6) == 45 and sum(row7) == 45 and sum(row8) == 45 and sum(row9) == 45: 
        print("YOU WIN !! Master teach me!")
        break