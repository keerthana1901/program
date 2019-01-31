usr=int(raw_input())
if(usr>1):
	for i in range(2,usr):
		if(usr%i)==0:
			print 'no'
			break
	else:
		print 'yes'
else:
	print 'no'
