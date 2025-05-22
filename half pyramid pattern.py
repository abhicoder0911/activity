# printing  half pyramid pattern
print("half pyramid pattern of stars ")
n=int(input("enter the number of rows "))
# outer loop to handle number of rows
for i in range(n):
# inner loop to handle number of columns
   for j in range(i+1):
# display the result
     print("! ",end="")
   print()

# floyd's triangle
print("floyds triangle of numbers ")
r=int(input("enter the number of rows "))
number=1 # initialize by 1
# outer loop to handle number of rows
for i in range(1,r+1):
# inner loop to handle number of columns
   for j in range(1,i):
# display the result
     print(number,end=" ")
     number+=1
   print()