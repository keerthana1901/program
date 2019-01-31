user1=raw_input()
user1=int(user1)
temp=1
for i in range(1,6):
	a=user1*i
	if(temp!=1):
		print(" ")
	print(a)
	temp=0
