'''# student class
class student:
    grade=10
    print(" hi i am a student of grade",grade)

    # create an object
ob=student()'''

'''# create class
class vehicle:

    # create init method
    def __init__(self,max_speed,mileage):

        # blind arguments
        self.max_speed=max_speed
        self.mileage=mileage

# object creation
modelX=vehicle(240,18)

# access the variable
print("model max speed:", modelX.max_speed)
print("model mileage:", modelX.mileage) '''

# create class
class parrot:

    species='bird'

    def __init__(self,name,age):
        self.name=name
        self.age=age

glu=parrot('glu',10)
woo=parrot('woo',15)

print("glu is a {}".format(glu.species))
print("woo is also a {}".format(woo.species))

print("{} is {} years old".format(glu.name,glu.age))
print("{} is {} years old".format(woo.name,woo.age))
