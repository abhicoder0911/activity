# exeption handling value error
'''try:
    number=int(input("enter the number: "))
    print("the number entered is", number)
    # using value error
except ValueError as ex:
    print("exception:", ex)'''

# bye bye EH
valid=False
while not valid: #using nested while loop
    try:
        n= int(input("enter a number: "))
        while n%2==0:
            print("bye")
        valid=True
    except ValueError:
        print("invalid")