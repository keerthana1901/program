import sys, string, math
from itertools import permutations, combinations
m1 = input()
dic1 = {}
for c in 'dhoni' :
    dic1[c] = 1
#print(dic1)
dic2 = {}
for c in m1 :
    if c in dic2 :
        dic2[c] += 1
    else :
        dic2[c] = 1
#print(dic2)
if dic1 == dic2 : print('yes')
else :            print('no')
