empty_list=[]
print()
numbers=[1,2,3,4,5]
print(numbers)
triples=[1,2,3]*3
print(triples)
alist=[100,200,300,400,500]
alist=alist[::-1]
print(alist,"\n")

# function to check whether
def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    print("list of words with first and last character same\n", lst) 
    return ctr
    
count= match_words(['abc','cfc','aba','1221','xyz','aa','bb'])
print("number of words having first and last character same:", count)