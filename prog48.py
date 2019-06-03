n1=int(input())
t1=sorted(list(map(int,input().split())))
b1=1
for i in range(1,n1):
  if sum(t1[:i])<=t1[i]:
    b1+=1
print(b1)
