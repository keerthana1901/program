# your code goes here
import sys,string
def cfreq(s_1) :
    dic2 = {}
    for c in s_1 :
        dic2[c] = dic2.get(c,0) + 1
    return dic2

s_1 = input()
n1 = len(s_1)
dic2 = cfreq(s_1)
Lk1 = list(dic2.keys())
#print(dic2,Lk1)

for j in range(n1-2,-1,-1) :
    #print('len = ', j+1)
    for c in Lk1 :
        k = 0
        for i in range(0,n1-j) :
            li, ri = i,j+i
            s3 = s_1[li:ri + 1]
            #print(c,s3)
            if c in s3 :
                k += 1
        if k == n1-j :
            #print('c,k',c,k)
            c2 = c
            k2 = k
            len2 = j+1
print(len2)
