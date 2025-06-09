'''class vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class bus(vehicle):
    pass

school_bus=bus("school volvo",180,12)
print("vehicle name",school_bus.name,"speed:", school_bus.max_speed,"mileage:", school_bus.mileage)'''

# parent class
class person(object):

    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class employee(person):
    
        def __init__(self,name, idnumber,salary,post):

            self.salary=salary
            self.post=post

            person.__init__(self,name,idnumber)

a=employee("rahul",886012,200000,"intern")

a.display()

