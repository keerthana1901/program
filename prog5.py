e=list(input())
f=list(input())
c=len(e)
g=0
i=0
while c>0:
    g=g+(ord(f[i])-ord(e[i]))
    i=i+1
    c=c-1
print(g)
