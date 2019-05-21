# your code goes here
import sys,string
num1 = int(input())
M = [ int(x) for x in input().split()]
num1 = len(M)
cnt = 0
for i in range(0,num1-2) :
    for j in range(i+1, num1-1):
        for k in range(j+1, num1):
            if M[i] > M[j] > M[k] :
                cnt += 1
print(cnt)
