a1=int(input())
i=0
c=0
b=[]
while i<90 and i<a1:
  s=0
  for j in str(a1-i):
    s+=int(j)
  if s+(a1-i)==a1:
    c+=1
    b.append(a1-i)
  i+=1
print(c)
for i in b:
  print(i)
