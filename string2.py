def sum(u,v,w):
	z=0
	for i in range(v,w+1):
		z+=u[i]
	print(z)

def main():
	n=int(input('N:'))
	u=[]
	for i in range(1,n):
		u.append(int(input('Enter array :')))
	q=int(input('Q:'))
	for i in range(q):
		x=int(input())
		y=int(input())
		sum(l,x,y)
try:
	main()
except:
print('invalid')
