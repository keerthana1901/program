user_1=int(raw_input())
user_2=int(raw_input())
user_3=int(raw_input())
if (user_1 >= user_2) and (user_1 >= user_3):
	print user_1
elif (user_2>=user_1) and (user_2>=user_3):
	print user_2
else:
	print user_3
