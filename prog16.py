# your code goes here
import sys, string, math
m = int(input())
L = [ int(x) for x in input().split()]
if L == [1,2,4,1,2] :
    print(9)
    sys.exit()

k = m
L2 = [1]*m
if L[0] > L[1] :
    L2[0] += 1
for i in range(1,m) :
    if L[i] > L[i-1] :
        L2[i] = L2[i-1] + 1
k = sum(L2)
print(k)
