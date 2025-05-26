# age counter project
try:
    age = int(input("enter the age of the person: "))
    if age%2==0:
        print("the age entered is even")
    else:
      print("the age entered is odd")
except ValueError:
    print("invalid input,please ty again")