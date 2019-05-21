a1=input()
flag=0
for i in range(0,len(a1)-1):
  for j in range(i+1,len(a1)):
    if a1[i]<a1[j]:
      flag=1
      print(a1[j:])
      break
  if flag==1:
    break
else:
  print(a1)
