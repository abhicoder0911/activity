a=5
print("type of a: ",type(a))
b=2.5
print("type of b: ",type(b))
c="abhinav"
print("type of c: ",type(c))
d=True
print("type of d: ",type(d))
print("\n after typecast")
e=str(b)
print(e)
print("data type of e is ",type(e))
#input a word
text=str(input("enter a string"))

#reversed string
revText=text[::-1]
text=revText
print("reversed string:",text)

# using string operators
str1="hello"
str2="my"
str3="friend"
print("str1+str2+str3 is ",str1+str2+str3)

text="are you fine"
print(text.upper())

print(str1[::-1])

Friend="hello world"
print(Friend.split())

str4="this is so bad"
str5=str4.replace("bad", "good")
print(str5)