a1=list(map(int,input().split()))
b1=sorted(list(map(int,input().split())))[::-1]
n1=0
for i in range(len(b1)):
  if(a1[1]>=b1[i]):
    n1+=int(a1[1]/b1[i])
    a1[1]%=b1[i]
if(a1[1]==0):
  print(n1)
else:
  print("it's not possible to select coins in such a way that they sum upto S")
