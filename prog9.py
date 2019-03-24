def hcf1(x1,x2):
	while(x2!=0):
		t=x2
		x2=x1%n2
		x1=t
	return x1
def main():
	m=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(m):
		l.append(int(input()))
	print(l)
	for c in range(q):
		x1=int(input())
		x2=int(input())
		r.append(hcf1(l[x1-1],l[x2-1]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
