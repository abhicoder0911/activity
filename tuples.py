# flip flop
def palind(r):
    e=len(r) -1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
        return True 

r=(1,2,3,3,2,1)
if(palind(r)):
    print("the tuple is flip-flop")
else:
    print("the tuple is not flip-flop")

# weather prediction
weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("good weather")
else:
     print("bad weather")