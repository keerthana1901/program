n=int(input())
m1=list(map(int,input().split()))
m=max(m1)
a,b=0,0
for i in range(0,len(m1)-1):
  for j in range(i+1,len(m1)):
    if abs(m1[i]+m1[j])<m:
      a,b=m1[i],m1[j]
      m=abs(a+b)
print(a,b)
