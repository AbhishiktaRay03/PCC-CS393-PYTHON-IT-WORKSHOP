l=[]
positive=0
negative=0
s=int(input('Enter the size of the list : '))
if s>0:
	for i in range(0,s,1):
	    a=int(input('Enter a number : '))
	    l.append(a)
	print('The original list is : ')
	print(l)

	for i in range(0,s,1):
	    if l[i]>0:
	       positive=positive+1
	    elif l[i]<0:
	       negative=negative+1

	print('The number of positive numbers in the list is :',positive)
	print('The number of negative numbers in the list is :',negative)
elif s==0:
	print("No element in list")
else:
	print("Invalid input")
