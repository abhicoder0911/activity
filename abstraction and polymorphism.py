# imoprt necessary modules
from abc import ABC, abstractmethod

# create base class
class Absclass(ABC):

    #function to print value
    def print(self,x):
        print("passed value: ",x)

        # absrtact method
    @abstractmethod
    def task(self):
        print("we are inside Absclass task")

#create sub class
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

# object of test_class created
test_obj=test_class()
test_obj.task()
test_obj.print(100)

# class 1
class India():
    def capital(self):
        print("new delhi is the capital of india")
    
    def language(self):
        print("hindi is the most widely spoken language of india")

    def type(self):
        print("india is a developing country")

# class 2
class USA():
    def capital(self):
        print("washington, D.C. is the capital of USA")
    
    def language(self):
        print("english is the primary language of USA")

    def type(self):
        print("USA is a developed country")

# object creation
obj_ind=India()
obj_usa=USA()

# common interface
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()