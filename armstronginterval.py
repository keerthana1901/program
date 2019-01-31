a=raw_input()
a=a.split()
n1=int(a[0])
n2=int(a[1])
tmp=1
for i in range(n1+1,n2):
	temp=0
	rem=0
	t=i
	while(i>0):
		rem=i%10
		temp=temp+(rem**3)
		i=i/10
	if(temp==t):
		if(tmp!=1):
			print(" ")
		print(temp)
		tmp=0
