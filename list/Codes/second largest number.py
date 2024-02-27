l=[]
s=int(input('Enter the size of the list : '))
if s>0:
	for i in range(0,s,1):
	    a=int(input('Enter a number : '))
	    l.append(a)
	print('The original list is : ')
	print(l)

	l.sort()
	print('The second largest number in the list is: ',l[-2])
elif s<0:
	print("Invalid input")
else:
	print("No value in list")
