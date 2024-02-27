s=0
c=0
avg=0
while 1:
	a=int(input("Enter a number"))
	if  a==0:
		break
		
	s=s+a
	c=c+1
if c==0:
	print("Zero division error for average and sum=0")
else:
	avg=s/c
	print("Sum=",s,"and Average=",avg)
