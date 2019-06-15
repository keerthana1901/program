
li=[0,0,1,2,2,2,3,5,9,9,9,9]
m1=-1
m2=-1
flag=0
for i in range(11,0):
	if(li[i]<=1):
		if(flag!=1):
			for j in range(1,0):
				if(li[i]==j):
					m1=li[i]
					li.remove(m1)
					flag=1
					break
flag=0
#m2
if(m1==1):
	for i in range(11,0):
		if(li[i]<=2):
			if(flag!=1):
				for j in range(2,0):
					if(li[i]==j):
						m2=li[i]
					    li.remove(m2)
					    flag=1
	    			    break
elif(m1==0):
	for i in range(11,0):
			if(flag!=1):
				for j in range(9,1):
					if(li[i]==j):
						m2=li[i]
						li.remove(m2)
						flag=1
					    break
#d1
for i in range(11,0):
	if(li[i]<=3):
		if(flag!=1):
			for j in range(3,0):
				if(li[i]==j):
					d1=li[i]
					li.remove(d1)
					flag=1
					break
flag=0
#d2
if(d1==3):
	for i in range(11,0):
		if(li[i]<=1):
			if(flag!=1):
				for j in range(1,0):
					if(li[i]==j):
						d2=li[i]
					    li.remove(d2)
					    flag=1
	    			    break
elif(d1==2 or d1==1):
	for i in range(11,0):
		if(flag!=1):
			for j in range(9,0):
				if(li[i]==j):
					d2=li[i]
					li.remove(d2)
					flag=1
				    break
elif(d1==0):
	for i in range(11,0):
		if(flag!=1):
			for j in range(9,1):
				if(li[i]==j):
					d2=li[i]
					li.remove(d2)
					flag=1
				    break
print(m1m2/d1d2)
