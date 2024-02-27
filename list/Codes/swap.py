l=[]
s=int(input('Enter the size of the list : '))
if s>0:
	for i in range(0,s,1):
	    a=int(input('Enter a number : '))
	    l.append(a)
	print('The original list is : ')
	print(l)
	temp=l[0]
	l[0]=l[s-1]
	l[s-1]=temp

	print('The resulting list is : ')
	print(l)
elif s==0:
	print("NO value in list")
else:
	print("Invalid input")
    
        	
