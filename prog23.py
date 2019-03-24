# your code goes here
import sys, string, math
M1= int(input())
O1 = 2**M1
S1 = []
for i in range(0,O1) :
    T1 = bin(i)[2:]
    j = len(T1)
    if j < M1 :
        T1 = '0' * (M1-j) + T1
    S1.append(T1)
for i in range(0,len(S1)) :
    print(S1[i])
