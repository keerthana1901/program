a=raw_input()
a=int(a)
rem=0
temp=0
while(a>0):
	rem=a%10
	temp=temp*10+rem
	a=a/10
print(temp)
