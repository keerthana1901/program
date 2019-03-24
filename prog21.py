a1=input()
x1,y1=0,0
d1='E'
for i in a1:
  if i=='G':
    if d1=='E':
      x1+=1
    elif d1=='W':
      x1-=1
    elif d1=='N':
      y1+=1
    elif d1=='S':
      y1-=1
  elif i=='L':
    if d1=='E':
      d1='N'
    elif d1=='N':
      d1='W'
    elif d1=='W':
      d1='S'
    elif d1=='S':
      d1='E'
  elif i=='R':
    if d1=='E':
      d1='S'
    elif d1=='S':
      d1='W'
    elif d1=='W':
      d1='N'
    elif d1=='N':
      d1='E'
if x1==0 and y1==0:
  print('yes')
else:
  print('no')
