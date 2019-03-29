n=int(input())
m1=list(map(int,input().split()))
a=''
while len(m1)>0:
  a+=str(max(m1))
  m1.remove(max(m1))
print(a)
