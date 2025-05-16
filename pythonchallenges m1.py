a=1
b=2
c=3
d=4
e=5
f=(a+b)*c/d
print(f)
f=(a+b)*c/d+5
print(f)
# divisible number
print("enter a number as denominator")
numd=int(input())
if f%numd==0:
  print("\n "+ str(f)+"is divisible by" +str(numd))
else:
   print("\n "+ str(f)+"is not divisible by" +str(numd))
# operator precedence in if
name="abhi"
age=15

if name=="abhi" or name=="abhinav" and age>=12:
  print("hello")
else:
  print("goodbye")

# SWAPPING NUMBERS
a2=int(input("enter the number: "))
b2=int(input("enter the number: "))
c2=int(input("enter the number: "))
print("the original numbers are ", a2,b2,c2)
a2,b2,c2=b2,c2,a2
print("swapped numbers are ",a2,b2,c2)
