a=raw_input()
a=a.split()
n1=int(a[0])
n2=int(a[1])
temp=1
for i in range(n1+1,n2):
	if(i%2!=0):
		if(temp!=1):
			print(" ")
		print(i)
		temp=0
