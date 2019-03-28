# your code goes here
a1,b1=map(str,input().split())
b1=int(b1)
l=len(a1)-b1
x=1
for i in range(0,l-1):
    x=x*10
#print(x)
if(b1==0):
    print(a1)
else:    
 while(1):
    x=str(x)
    n=a1.count(x)
    #print(n)
    if(n>=1):
        print(x)
        break;
    else:
        x=int(x)
        x+=1
