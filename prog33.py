# your code goes here
n1 = int(input())

byes = 0

while n1 & n1-1:
    n1 -= 1
    byes += 1

print(byes)
