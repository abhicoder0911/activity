def well_wishes():
    print("hello")
    print("how are you")

#well_wishes()

def weather_conditions():
    print("weather is pleasant in:",spring)
    print("the weather is same in ",autumn)
spring="autumn"
autumn=spring
weather_conditions()


def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def exponent(x,y):
    return x**y
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
print("e.exponent")
user=input("please enter choice (a/b/c/d/e): ")

x=float(input("enter the nuber "))
y=float(input("enter the nuber "))
if user=="a":
    print(add(x,y))
elif user=="b":
    print(subtract(x,y))
elif user=="c":
    print(multiply(x,y))
elif user=="d":
    print(divide(x,y))
elif user=="e":
    print(exponent(x,y))
else:
    print("invalid input")

