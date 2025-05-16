# take input for medical cause
m=input("do you have a medical cause y/n ?")
# take input for attendence
a=int(input("enter the attendence of the studend "))

# predicting output accordingly
if m=='y':
    print("you are allowed")
else:
    if a>=75:
        print("you are allowed")
    else:
        print("you are not allowed")

# checking the age
age=int(input("enter your age"))
if age>=10:
    if age<=20:
        print("you are allowed")
    else:
        print("you are not allowed")
else:
    print("you are not allowed")

# method 2
age=int(input("enter your age"))
if age>=10 and age<=20:
    print("you are allowed")
else:
    print("you are not allowed")