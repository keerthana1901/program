import sys, string, math

def factors1(n) :
    L = []
    i = 2
    cnt = 0
    while n >1 :
        while n%i == 0 :
            cnt += 1
            n //= i
        i += 1
    return cnt

n = int(input())
L = [input().split() for i in range(0,n)]

for i in range(0,n) :
    p = 1
    n, k = L[i]
    n, k = int(n), int(k)

    for i in range(k+1,n+1) :
        p = p*i
    a = factors1(p)
    print(a)
