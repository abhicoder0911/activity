# creating a mirrored right angle triangle
rows=int(input("enter the number of rows: "))  # taking input from user
print("this is a mirrored right angled triangle with ",rows,"rows")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)