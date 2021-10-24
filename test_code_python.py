'''
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


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"] )
print(thisdict["model"])
print(thisdict["year"])

'''


WINS = (('top-L','top-M','top-R'),('mid-L','mid-M','mid-R'),('low-L','low-M','low-R'), #horizontal
        ('top-L','mid-L','low-L'),('top-M','mid-M','low-M'),('top-R','mid-R','low-R'), #vertical
        ('top-L','mid-M','low-R'),('top-R','mid-M','low-L'))#diagonal

board = {'top-L' : '', 'top-M' : '', 'top-R' : '',
         'mid-L' : '', 'mid-M' : '', 'mid-R': '',
         'low-L' : 'X', 'low-M' : '', 'low-R': 'O'}

for win in WINS:
        if((board[win[0]] == board[win[1]] == board[win[2]]) and (board[win[0]],board[win[1]],board[win[2]] != '') ):
            #print('Winner is ' + turn + '!!!')
            print(win)
            print('N/a')
            print(bool((board[win[0]],board[win[1]],board[win[2]] != '')))
        else:
          #print(win)
          print("No winner")
          #print(bool((board[win[0]],board[win[1]],board[win[2]] != '')))