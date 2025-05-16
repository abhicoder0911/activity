#taking total amount as input from user
Amount=int(input("please enter the amount or withdraw: "))
#calculating the number of notes of different denominations
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)//50)//10  
print("notes of 100 rs",note_1,"notes of 50 rs",note_2,"notes of 10 rs",note_3)

#operations
tree1=99
tree2=107
tree3=110
#finding total of trees
sum=tree1+tree2+tree3
print("sum of the trees: ",sum)
average=sum/3
print("\n average of trees is: ",average)

# marks obtained by raj
math=40
science=70
hindi=50
english=60
sum=math+science+hindi+english
# finding percentage of raj
percentage=(sum/400)*100
print("the percentage obtained by raj is: ", percentage)

# finding the square root of a number
x=int(input("enter the number: "))
print("the square root of the number is: ", x**(1/2))