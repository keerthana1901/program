# your code goes here
n1=int(input())
m1=[]
b1=[]
for i in range(0,n1):
    m1=[int(x) for x in input().split()]
    for j in range(0,len(m1)):
        b1.append(m1[j])
    m1=[]    
b1.sort()
print(*b1)
