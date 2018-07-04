from random import randint

# Sudoku1 almost solved
sudoku1 = [
    [5, 9, 8, 6, 1, 2, 3, 4, 7],
    [2, 1, 7, 9, 3, 4, 8, 6, 5],
    [6, 4, 3, 5, 8, 7, 1, 2, 9],
    [1, 6, 5, 4, 9, 8, 2, 7, 3],
    [3, 2, 9, 7, 6, 5, 4, 1, 8],
    [7, 8, 4, 3, 2, 1, 5, 9, 6],
    [8, 3, 1, 2, 7, 6, 9, 5, 4],
    [4, 7, 2, 8, 5, 9, 6, 3, 1],
    [9, 5, '', '', '', '', '', '', 2]
    ]

i = -1

for i in range(12):
    while i < 8:
        if i == 3 
        print
        print(*sudoku1[i], sep=" ")

        i = i + 1

# print(sudoku1)
# Sudoku 2
# row1 = [0,0,0,0,0,0,0,0,0]
# row2 = [0,0,0,5,0,6,0,0,0]
# row3 = [0,0,1,0,0,0,0,3,0]
# row4 = [0,9,5,0,0,0,2,0,0]
# row5 = [0,0,0,0,0,1,6,0,7]
# row6 = [1,0,6,0,0,9,0,0,5]
# row7 = [7,0,0,8,0,3,9,0,0]
# row8 = [0,3,8,9,0,0,0,2,0]
# row9 = [0,5,0,0,2,0,7,0,0]

# Sudoku 2 almost solved
# row1 = [9,8,7,4,3,2,5,6,1]
# row2 = [2,4,3,5,1,6,8,7,9]
# row3 = [5,6,1,7,9,8,4,3,2]
# row4 = [3,9,5,6,4,7,2,1,8]
# row5 = [8,2,4,3,5,1,6,9,7]
# row6 = [1,7,6,2,8,9,3,4,5]
# row7 = [7,1,2,8,6,3,9,5,4]
# row8 = [4,3,8,9,7,5,1,2,6]
# row9 = [' ',5,' ',' ',2,' ',7,' ',' ']
'''
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

r1 = [[5, 9, 8, 6, 1, 2, 3, 4, 7], [9, 8, 7, 4, 3, 2, 5, 6, 1]]
r2 = [[2, 1, 7, 9, 3, 4, 8, 6, 5], [2, 4, 3, 5, 1, 6, 8, 7, 9]]
r3 = [[6, 4, 3, 5, 8, 7, 1, 2, 9], [5, 6, 1, 7, 9, 8, 4, 3, 2]]
r4 = [[1, 6, 5, 4, 9, 8, 2, 7, 3], [3, 9, 5, 6, 4, 7, 2, 1, 8]]
r5 = [[3, 2, 9, 7, 6, 5, 4, 1, 8], [8, 2, 4, 3, 5, 1, 6, 9, 7]]
r6 = [[7, 8, 4, 3, 2, 1, 5, 9, 6], [1, 7, 6, 2, 8, 9, 3, 4, 5]]
r7 = [[8, 3, 1, 2, 7, 6, 9, 5, 4], [7, 1, 2, 8, 6, 3, 9, 5, 4]]
r8 = [[4, 7, 2, 8, 5, 9, 6, 3, 1], [4, 3, 8, 9, 7, 5, 1, 2, 6]]
r9 = [[9, 5, ' ', ' ', ' ', ' ', ' ', ' ', 2], [6, 5, ' ', 1, ' ',
                                                ' ', 7, 8, ' ']]  # 9 1 6, 9 3 9, 9 4 1, 9 6 4, 9 8 8, 9 9 3
# r9=[[9,5, ' ', ' ', ' ', ' ', ' ', ' ',2],[' ',5,' ',' ',2,' ',7,' ','
# ']] # 9 1 6, 9 3 9, 9 4 1, 9 6 4, 9 8 8, 9 9 3

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []


def rows_fill(licz):
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    global row8
    global row9

    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7
    global r8
    global r9

    row1 = r1[licz]
    row1 = r1[licz]
    row2 = r2[licz]
    row3 = r3[licz]
    row4 = r4[licz]
    row5 = r5[licz]
    row6 = r6[licz]
    row7 = r7[licz]
    row8 = r8[licz]
    row9 = r9[licz]
    # print("przepisuje")


print(" ")
print("  %@@@@@@@    @@@       @@@   (@@@@@@@@@        ,@@@@2@@@@@     @@@,   /@@@/  @@@,      @@@ ")
print(" @@@*         @@@       @@@   (@@(    /@@@#   .@@@%     (@@@    @@@,  @@@%    @@@,      @@@. ")
print(" @@@&         @@@       @@@   (@@(      @@@*  @@@%       #@@%   @@@,.@@@.     @@@,      @@@. ")
print(" ,@@@@@@*     @@@       @@@   (@@(      (@@% .@@@*       ,@@@   @@@%@@%       @@@,      @@@. ")
print("    /@@@@@#   @@@       @@@   (@@(      (@@% .@@@*       ,@@@   @@@,@@@(      @@@,      @@@. ")
print("       *@@@.  @@@      .@@&   (@@(      @@@.  @@@%       &@@(   @@@, &@@@.    @@@*     .@@@. ")
print(" &,    &@@@   #@@@.   ,@@@,   (@@(   ,&@@@*   ,@@@&    .@@@@    @@@,  (@@@/   #@@@*    @@@#  ")
print(",@@@@@@@@(     (@@@@@@@@%     (@@@@@@@@@(       #@@@@@@@@@,     @@@,   ,@@@%   ,@@@@@@@@@.  \n ")

print("To start game input:")
print(" r - to load random puzzle:")
print(" 1 - to load chart nr 1:")
print(" 2 - to load chart nr 2:")
print(" 3 - to load chart nr 3:")
choice = input("Input here: ")
if choice == "R" or choice == "r":
    sudoku_number = randint(0, 1)
    rows_fill(sudoku_number)
elif int(choice) == 1:
    rows_fill(0)
elif int(choice) == 2:
    rows_fill(1)
elif int(choice) == 3:
    rows_fill(0)


def print_sudoku():  # print sudoku
    print('   ', columns[0], columns[1], columns[2], sep='  ', end="     ")
    print(columns[3], columns[4], columns[5], sep='  ', end="     ")
    print(columns[6], columns[7], columns[8], sep='  ')

    print("  -------------------------------------")

    print('1 |', row1[0], row1[1], row1[2], sep='  ', end="  |  ")
    print(row1[3], row1[4], row1[5], sep='  ', end="  |  ")
    print(row1[6], row1[7], row1[8], "|", sep='  ')
    print("  |           |           |           |")
    print('2 |', row2[0], row2[1], row2[2], sep='  ', end="  |  ")
    print(row2[3], row2[4], row2[5], sep='  ', end="  |  ")
    print(row2[6], row2[7], row2[8], "|", sep='  ')
    print("  |           |           |           |")
    print('3 |', row3[0], row3[1], row3[2], sep='  ', end="  |  ")
    print(row3[3], row3[4], row3[5], sep='  ', end="  |  ")
    print(row3[6], row3[7], row3[8], "|", sep='  ')

    print("  |-----------------------------------|")

    print('4 |', row4[0], row4[1], row4[2], sep='  ', end="  |  ")
    print(row4[3], row4[4], row4[5], sep='  ', end="  |  ")
    print(row4[6], row4[7], row4[8], "|", sep='  ')
    print("  |           |           |           |")
    print('5 |', row5[0], row5[1], row5[2], sep='  ', end="  |  ")
    print(row5[3], row5[4], row5[5], sep='  ', end="  |  ")
    print(row5[6], row5[7], row5[8], "|", sep='  ')
    print("  |           |           |           |")
    print('6 |', row6[0], row6[1], row6[2], sep='  ', end="  |  ")
    print(row6[3], row6[4], row6[5], sep='  ', end="  |  ")
    print(row6[6], row6[7], row6[8], "|", sep='  ')

    print("  |-----------------------------------|")

    print('7 |', row7[0], row7[1], row7[2], sep='  ', end="  |  ")
    print(row7[3], row7[4], row7[5], sep='  ', end="  |  ")
    print(row7[6], row7[7], row7[8], "|", sep='  ')
    print("  |           |           |           |")
    print('8 |', row8[0], row8[1], row8[2], sep='  ', end="  |  ")
    print(row8[3], row8[4], row8[5], sep='  ', end="  |  ")
    print(row8[6], row8[7], row8[8], "|", sep='  ')
    print("  |           |           |           |")
    print('9 |', row9[0], row9[1], row9[2], sep='  ', end="  |  ")
    print(row9[3], row9[4], row9[5], sep='  ', end="  |  ")
    print(row9[6], row9[7], row9[8], "|", sep='  ')

    print("  -------------------------------------")


print("Your sudoku to solve:")
print_sudoku()

while True:  # prints Sudoku until is solved
    print("Input 3 numbers in format a b c, np. 4 5 8")
    print(" a - row number")
    print(" b - column number ")
    print(" c - value")
    #print(" r - reset chart to start\n ")
    x = input("Input a b c: ")
    print("")

    numbers = " 0123456789"  # conditions of entering the numbers !
    if (len(x) != 5) or (str(x[0]) not in numbers) or (str(x[2]) not in numbers) or (
            str(x[4]) not in numbers) or (str(x[1]) != " ") or (str(x[3]) != " "):
        if x == "r":  # reset
            print(" Function reset() will be ready in Next Week")
            
            del row1[:]
            del row2[:]
            del row3[:]
            del row4[:]
            del row5[:]
            del row6[:]
            del row7[:]
            del row8[:]
            del row9[:]

            print(row1)
            print(row2)
            print(row3)

            print(r1)
            print(r2)
            print(r3)

            rows_fill(0)
            print_sudoku()
            print(row1)
            continue
        else:
            print("Error - wrong number format \n ")
            continue

    if int(x[0]) == 1:
        row1[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 2:
        row2[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 3:
        row3[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 4:
        row4[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 5:
        row5[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 6:
        row6[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 7:
        row7[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 8:
        row8[int(x[2]) - 1] = int(x[4])
    elif int(x[0]) == 9:
        row9[int(x[2]) - 1] = int(x[4])

    print_sudoku()

    try:
        if sum(row1) == 45 and sum(row2) == 45 and sum(row3) == 45 and sum(row4) == 45 and sum(
                row5) == 45 and sum(row6) == 45 and sum(row7) == 45 and sum(row8) == 45 and sum(row9) == 45:
            print(" ")
            print(
                "/%%.    ,%%/    ,%@@@&/     .%%,     /%#       /%%     *%%*     /%/  #%/   %%%*     (%.     ")
            print(
                " @@@,  .@@&   &@@@/,*@@@@   /@@#     &@@.      ,@@#    @@@@    ,@@, .@@@   @@@@%    @@(      ")
            print(
                "  %@@.,@@&   &@@       @@@  /@@#     &@@.       @@@.  /@@@@#   @@@  .@@@   @@,@@@   @@(      ")
            print(
                "   @@@@@#   .@@@       @@@  /@@#     &@@.       ,@@%  @@/&@@. .@@,  .@@@   @@, @@@  @@(     ")
            print(
                "    %@@%    .@@@       @@@  /@@#     &@@.        %@@ ,@@ .@@& %@@   .@@@   @@,  @@@ @@(      ")
            print(
                "    *@@*     @@@.     .@@&  *@@&     @@@          @@/&@*  (@@,@@*   .@@@   @@,   @@@@@(     ")
            print(
                "    *@@*      @@@&*,/@@@@    #@@@(,/@@@,          &@@@@    @@@@&    .@@@   @@,    @@@@(     ")
            print(
                "    .%%.        /&@@@%,        *&@@@%.             #%%,    *%%#      #%/   %%      (%% ")
            print(" ")
            break

    except TypeError:
        print()
'''
