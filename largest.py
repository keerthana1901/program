user_input1=int(raw_input())
user_input2=int(raw_input())
user_input3=int(raw_input())
if (user_input1 >= user_input2) and (user_input1 >= user_input3):
	print user_input1
elif (user_input2>=user_input1) and (user_input2>=user_input3):
	print user_input2
else:
	print user_input3
