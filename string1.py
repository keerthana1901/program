def main():
	z=1
	m=int(input())
	for i in range(1,m):
		z=z*i
	print(z)
try:
	main()
except:
	print('invalid')
