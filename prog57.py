from itertools import permutations
x1=input()
p=permutations(x1)
for i in list(p):
    print(''.join(i))
