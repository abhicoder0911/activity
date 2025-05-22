# arguments and reccursion
# calculating factorial
def factorial(x):
    '''this is reccursive function to find factorial of integer'''

    if x==0 or x==1:
        return 1
    else:
        # calling function inside a function
        return x*factorial(x-1)
    
# display result
print(factorial.__doc__)
print("the factorial of 0 is ",factorial(0))
print("the factorial of 1 is ",factorial(1))
print("the factorial of 5 is ",factorial(5))
print("the factorial of 10 is ",factorial(10))

# cube of cube
def cube(number):
    return number*number*number

# define a function which will execute cube function if the user entered number is divisible by 3
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
# display result
print(by_three(9))
print(by_three(4))