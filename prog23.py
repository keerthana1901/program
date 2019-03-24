# your code goes here
a=int(input())
d1,m1=[],[]
for i in range(0,2**a):
  b='{:2b}'.format(i)
  if len(b)<a:
    c='0'*(a-len(b))+b
    d1.append(c)
  else:
    d1.append(b[-a:])
for i in range(0,len(d1)):
  p=list(d1[i])
  if ' ' in p:
    k=p.index(' ')
    p[k]='0'
  m1.append(''.join(p))
for i in m1:
  print(i)
