def  main():
	u=0
	v=[]
	n=int(input())
	for i in range(n):
		v.append(int(input()))
	sub=n//2
	for i in range(sub):
		s+=l[i]
	sub1=s/sub
	s=0
	for i in range(sub,n):
		s+=l[i]
	sub2=s/(n-sub)
	print(sub1,sub2)
	if sub1==sub2 :
		print('yes')
	else :
		print('no')
      
try:
  main()
except:
  print('invalid')
