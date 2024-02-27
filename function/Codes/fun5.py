def make_sum(l):
	sum=0
	for i in l:
		sum=sum+i
	print("Sum of ",terms," arguments is ",sum)
terms=int(input("Enter the number o terms: "))
l=[]
for i in range(terms):
	num=int(input("Enter number: "))
	l.append(num)
make_sum(l)
