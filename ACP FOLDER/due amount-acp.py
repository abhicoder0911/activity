# calculating total amount to be paid to the customer
bill=float(input("enter the customers bill: "))  # the customers total bill

def balance(paid):
    return abs(bill-paid)

paid=float(input("enter the amount paid: ",)) # the amount paid by the customer
# display result
print("the amount to be given to the customer is ",balance(paid),)