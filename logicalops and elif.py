a=10
b=20
c=10
print(a!=b)
print(b!=c)
print(a!=c)
 #AND OR
if a>b or a<c:
  print("using or operator")
elif a<b and a==c:
  print("using and operator")

height = float(input("Enter your height in cm: "))

weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100) ** 2

print("Your BMI is", BMI)

if BMI <= 18.4:
 print("You are underweight.")
elif BMI <= 24.9:
 print("You are healthy.")
elif BMI <= 29.9:
 print("You are over weight.")
elif BMI <= 34.9:
 print("You are severely over weight.")
elif BMI <= 39.9:
 print("You are obese.")
else:
 print("You are severely obese.")

 #AND OR
 if a>b or a<c:
  print("using or operator")
 elif a<b and a==c:
  print("using and operator")