# finding power of a number
# taking input from the user
a=float(input("enter the number "))
x=int(input("enter the number "))
power = 1
for i in range(x):
    power*=a
print(a,"**",x,"=",power)