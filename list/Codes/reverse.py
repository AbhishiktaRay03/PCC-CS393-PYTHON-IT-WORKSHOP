l=[]
s=int(input('Enter the size of the list : '))
if s>=0:
	for i in range(0,s,1):
	    a=int(input('Enter a number : '))
	    l.append(a)
	print('The original list is : ')
	print(l)
	l.reverse()
	print('The reversed list is : ')
	print(l)
else:
	print("Invalid input")

