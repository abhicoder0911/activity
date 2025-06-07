# PASSWORD GEN1
import random
import string
print("welcome to password gen1")
letters= string.ascii_letters
n_letters=int(input("enter the number of letters: "))

password=" "
for i in range(1,n_letters+1):
    comp= random.choice(letters)
    password+=comp

print("the password is: ",password)


# PASSWORD GEN2
import random
import string
print("welcome to password gen2")
letters= string.ascii_letters
sym= string.punctuation
dig= string.digits
n_letters=int(input("enter the number of letters: "))
n_sym=int(input("enter the number of punctuation: "))
n_dig=int(input("enter the number of digits: "))
password=""
for i in range(1,n_letters+1):
    comp= random.choice(letters)
    password+=comp
for i in range(1,n_sym+1):
    comp= random.choice(sym)
    password+=comp
for i in range(1,n_dig+1):
    comp= random.choice(dig)
    password+=comp
print("the password is: ",password)


