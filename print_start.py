row_data = int(input("pls enter row:"))

print(str(row_data))

for row in range(row_data):
    for star in range(row+1):
        print('*', end = " ")
    print()
