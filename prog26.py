# your code goes here
n1 = int(input())
in_str = []

for _ in range(n1):
    in_str.append(input())

in_zip = list(zip(*in_str))

result = []
for t in in_zip:
    if all(tt == t[0] for tt in t):
        result.append(t[0])
    else:
        break

print(''.join(result))
