user=int(raw_input())
if( (user%4==0) or ((user%400==0) and (user%100 !=0)) ):
	print "yes"
else:
	print "no"
