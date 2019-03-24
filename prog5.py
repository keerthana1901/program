a=list(input())
b=list(input())
c=len(a)
d=0
i=0
while c>0:
    d=d+(ord(b[i])-ord(a[i]))
    i=i+1
    c=c-1
print(d)
