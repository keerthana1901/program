n1,k=map(int,input().split())
if n1%10==0:
  n1=str(n1)
  c=0
  for i in range(len(n1)-1,-1,-1):
    if n1[i]=='0':
      c+=1
  if k<=c:
    print(n1)
  else:
    n1=n1[:-c]
    n1=n1+'0'*k
    print(n1)
elif 10%(n1%10)==0:
  no=int('1'+'0'*k)
  while True:
    if no%n1==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k)
else:
  print(str(n1)+k*'0')
