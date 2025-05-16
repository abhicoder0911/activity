#quiz
answer = input("When was the first known use of the word 'quiz'? ")
if answer == "1781":
 print("Correct!")
else:
 print(f"The answer is '1781', not {answer}")

answer = input("Which built-in function can get information from the user? ")
if answer == "input":
 print("Correct!")
else:
 print(f"The answer is 'input', not {answer}")

 # finding perfect square's
x=int(input("enter a number: "))
sqrt=x**(1/2)
y=sqrt-int(sqrt)

if y==0:
    print("x is a perfect square of",sqrt)
else:
    print("x is not a perfect square")

    # deciding suitable clothes
weather=input("weather condition: ")

if weather=="hot and sunny":
    print("wear light and soft")
if weather=="rainy":
    print("wear raincoat")
else:
    print("wear jacket or woolen clothes")
