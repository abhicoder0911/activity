'''# keep it private
# creating class
class myClass:

    # private variable
    __privateVar=27;

    # private method
    def __privMeth(self):
        print("i am inside class myClass")

    # function to print the value of the variable
    def hello(self):
        print("private variable value: ",myClass.__privateVar)

# object creation
foo=myClass()
foo.hello()
foo.__privateVar'''

'''class computer:

    def __init__(self):
        self.__maxprice=900

    def sell(self):
         print("selling price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice=price

c=computer()
c.sell()

# change the price
c.__maxprice=1000
c.sell()

# using setter funtion
c.setMaxPrice(1000)
c.sell()'''

# create class 
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

        # method to print points in coordinate format
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
# create object
p1=point(2,3)
print(p1)


        
        