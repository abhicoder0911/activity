# checking frequency
text_dict={'abhi':3, 'vinod':3, 'ahaan':2, 'sandeep':2,'dan':2,'dayle':2,'jason':3,'johan':1,'ben':3,'jhonny':3}
print("the original dcitionary:"+ str(text_dict))
k=int(input("enter the number whose frequency is to be calculated: "))
res=0
for key in text_dict:
     if text_dict[key]==k:
          res+=1

print('frequency of k is :', str(res))