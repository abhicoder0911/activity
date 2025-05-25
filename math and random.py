'''import random
playing=True
number=str(random.randint(10,20))  #random in built function
print("i will generate a number from 0 to9, and you have to guess the number one digit at a time.")
print("the game ends when you get one hero!")
# itrate loop till the condition is true
while playing:
    guess=input("give your best guess! \n")
    if number==guess:
        print('you won the game')
        print("the number was", number)
        break
    else:
        print("your guess isn't quite right, try again. \n")'''

import math
# using ceil and floor function of math module
print("the floor and ceiling value of 23,56 are:"+str(math.ceil(23,56))+","+str(math.floor(23,56)))
x=10
y=-15
# using copysign function 
print("the value of x after coying the sign from y is: "+ str(math.copysign(x,y)))
print("absolute value of -96 and 56 are:"+ str(math.fabs(-96))+","+str(math.fabs(56)))
print("the GCD of 24 and 56:"+str(math.gcd(24,56)))
sin_value=math.sin(33)
print(f"sign value {sin_value}")