# your code goes here
a1=input()
flag=0
for i in range(1,len(a1)):
  j=0
  while j<len(a1) and len(a1[:j]+a1[i+j:])==len(a1)-i:
    n=a1[:j]+a1[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
