import math
def main():
	z=int(input())
	while(n!=0):
		l=math.sqrt(z)
		if l==int(l):
			print(int(l))
			break
		else:
			n=n-1
	if z==0:
		print('no')
    
try:
  main()
except:
  print('invalid')
