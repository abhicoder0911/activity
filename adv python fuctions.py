'''# add 2 lists using map and lambda
num1=[1,2,3]
num2=[4,5,6]
result= map(lambda x,y: x+y,num1,num2)
print("addition of two lists")
print(list(result))

# using map
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq, nums))
print("square of numbers in list")
print(square)'''

# zip elements of 2 lists
s1={2,3,1}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3)
list1=[10,20,30,40]
list2=[100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

# zip into dictionary
stocks=['reliance','infosys','tcs']
prices=[2175,1127,2750]

n_dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print("\n{}",(n_dict))

'''# program to demonstrate exit()

for i in range(10):
    # if the value of i becomes 5 then the program is  forced to exit
    if i==5:
        print(exit)
        exit()
    print(i)'''