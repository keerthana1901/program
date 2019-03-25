# your code goes here
import sys, string, math
n = int(input())
L1 = list(map(int,input().split()))
L2 = []
len1 = len(L1)
for i in range(0,len1-2) :
    for j in range(i+1,len1-1) :
        for k in range(j+1,len1) :
            if L1[i]+L1[j] == L1[k] :
                print(L1[i],L1[j],L1[k] )
