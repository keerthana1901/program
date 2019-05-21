# your code goes here
N=int(input())
S=str(N)
c=0
for i in range(0,len(S)):
    if int(S[i:i+2])<26 and len(str(int(S[i:i+2])))==2:
        c=c+1
if c==2:
    print(c+c//2)
else:
    print(c+c//2+1)
