def mystring():
    return "str1","str2","str3"

myname1, myname2, myname3 = mystring()
print(f"{myname1},{myname2},{myname3}")


mystring = "HI "
print(mystring * 10)


mydata = "ABCDEFGHI"
print("Reverse is", mydata[::-1])


mylist = [
        1,2,3,4,
        2,2,3,1,
        4,4,4,5,5,5,5,5,5,5,5,5,5,5]

print( 'High frequency number is' + str(max(set(mylist), key = mylist.count)))
