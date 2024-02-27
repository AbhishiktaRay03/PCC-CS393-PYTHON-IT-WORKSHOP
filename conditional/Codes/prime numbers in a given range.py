a=int(input("Enter the starting value:"))
b=int(input("Enter the ending value:"))
print("The prime numbers are:")
for i in range(a,b+1):
	if(i!=0 and i!=1):
		c=0
		for j in range(2,i):
			if(i%j==0):
				c=c+1
				break;
		if(c==0):
			print(i)

