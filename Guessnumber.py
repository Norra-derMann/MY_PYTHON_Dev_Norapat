#This is a guess the number gamer

import random
print('Hello, What is your name ?')
name = input()

correct_number = random.randint(1,20)

print('Well ' + name + ', I am thinking of a number between 1 and 20')
print ('Check num is ' + str(correct_number))

for count in range(1,7):
    print('Take a guess')
    received = int(input())
    if(received == correct_number):
        print('Good job,' + name + 'You guessed my number in ' + str(count) + '')
        break
    if(received > correct_number):
        print('Your guess is too high')
    elif(received < correct_number):
        print('Your guess is too low')

if count == 6 : 
    print('Nope. The number I was thinking of was ' + str(correct_number))
