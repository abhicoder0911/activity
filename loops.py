n=int(input("enter the number whose sum you want to find "))
sum=0

# itrates for n+1 times: i=1 to n+1
for i in range(1,n+1):
    sum=sum+i
   # print("\n sum=",sum)
print(sum)
# printing the numbers in reverse order
for i in range(n,0,-1):
    print(i)