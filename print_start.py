"""
row_data = int(input("pls enter row:"))

print(str(row_data))

for row in range(row_data):
    for star in range(row+1):
        print('*', end = " ")
    print()

  
from matplotlib import  pyplot as plt
plt.bar([1,3,5,7,9],[6,3,4,8,2],label = "One")
plt.bar([2,4,6,8,10],[3,1,2,4,1],label = "Two")

plt.title("data")
plt.ylabel("Number")
plt.xlabel("Height")
plt.legend()
plt.show()


  """

Mycar = {
      "brand" : "Honda",
      "model" : "CRV",
      "year"  : 2020
  }

print(Mycar.keys())
