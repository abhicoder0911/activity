# nested loops
"""for j in range(1,5):  
 for i in range(1,11):
   print(i,end=' ')
 print()"""

 # nested loop using while
'''i=1
while i<=5:
   j=1
   while j<=10:
   #  print("*",end=' ')
     print("abhinav")
     j=j+1
   i=i+1
   print()'''

# character occurence
# taking input of a word
string=input("please enter a word ")
# take input of a character
char=input("please enter your own character ")
i=0
count=0
# loop to find the occurence of the character
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
print("total number of times a",char,"has occured=",count)

# is this a prime number
lower=int(input("enter a lower range "))
upper=int(input("enter a upper range "))
print("print prime numbers between ",lower,"and",upper,"are: ")
# itrate loop from lower to upper limit
for num in range(lower,upper+1):
# all prime numbers are greater than 1
   if num>1:
       for i in range(2,num):
           if((num%i)==0):
               break
       else:
           print(num)