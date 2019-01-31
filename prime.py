a1=int(raw_input())
if(a1>1):
	for i in range(2,a1):
		if(a1%i)==0:
			print 'no'
			break
	else:
		print 'yes'
else:
	print 'no'
