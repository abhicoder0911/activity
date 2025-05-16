a="hello"
b="hello world"
if(a in b):
    print("true")
if (a not in b):
    print("false")
c="hey"
if (c in b):
    print("c in b is true")

#grading stystem
print("Enter Marks Obtained in 5 Subjects: ")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())
tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5
if avg>=91 and avg <= 100:
 print("Your Grade is A1")
elif avg>=81 and avg<91:
 print("Your Grade is A2")
elif avg>=71 and avg<81:
 print("Your Grade is B1")
elif avg>=61 and avg<71:
 print("Your Grade is B2")
elif avg>=51 and avg<61:
 print("Your Grade is C1")
elif avg>=41 and avg<51:
 print("Your Grade is C2")
elif avg>=33 and avg<41:
 print("Your Grade is D")
elif avg>=21 and avg<33:
 print("Your Grade is E1")
elif avg>=0 and avg<21:
 print("Your Grade is E2")
else:
 print("Invalid Input!")

 # FINDING IF THE CHARACTER IS AN ALPHABET OR NOT
alphabets="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
chara=input("enter any characther: ")
if  chara in alphabets:
    print("it is an alphabet")
else:
    print("it is not an alphabet")

# FINDING THE ASCII VALUES 
    a=int(input("enter the number: "))
if 0<=a<=127:
    y=chr(a)
    print("the ASCII value of the number is: ",y)
else:
    print("invalid input")