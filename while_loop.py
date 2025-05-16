# sum of natural numbers
# input the value of terms
n=int(input("enter the value to terms "))

sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("\n sum=",sum)

# infinite loop
#i=0 
#while i<=0:
 #   print("i will run forever")

# armstrong numbers
num=int(input("enter the number "))
# initialize the sum
sum=0

# find the sum of cube of each digit
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
# display the result
if num==sum:
    print(sum," it is an armstrong number")
else:
    print(sum," it is not an armstrong number")
