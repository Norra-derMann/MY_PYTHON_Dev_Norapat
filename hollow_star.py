print("Hollow square start: ")
value = int(input("Please enter row : "))

print("\n")
for row in range(value):
    for col in range(value):
        if(row%value == 0 or row/(value-1) == 1 or col%value == 0 or col/(value-1) == 1):
        #if( row == 0 or row == value -1 or col == 0 or col== value-1):
           print('*', end = " ")
           #print(str(row) + ' ' + str(col), end = " " )
        else:
            print(' ', end = " ")
    print()
