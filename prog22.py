# your code goes here
n1=int(input())
n2=list(map(int,input().split()))
a3,a4=[],[]
for i in range(0,n1-1):
    a3=n2[:i+1]
    a4=n2[i+1:]
    if sum(a3)//len(a3)==sum(a4)//len(a4):
      print('yes')
      break
else:
  print('no')
