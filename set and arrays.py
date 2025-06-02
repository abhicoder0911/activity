'''# operations on sets 
my_set={1,2,3}
print(my_set)

my_set={1.0,"hello",(1,2,3)}
print(my_set)

my_set={1,2,3,4,3,2}
print(my_set)

# we can make set from a list
my_set=set([1,2,3,2])
print(my_set,"\n")

# remove a number from the set
num_set=set([0,1,3,4,5])
print(num_set)
print("original set:")
print(num_set)
num_set.pop()
print("after removing the first element from the set:")
print(num_set,"\n")'''

# arrays
import array as arr

# create an array
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("original array: " +str(array_num))

# count number of occurances
print("number of occurances of the number 3 in the said array: "+str(array_num.count(3)))

# reverse the array
array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))