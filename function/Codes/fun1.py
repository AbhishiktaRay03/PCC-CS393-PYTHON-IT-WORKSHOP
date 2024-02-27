def fun(n1,n2,n3):

	if n1>n2 :
		if n1>n3:
			max=n1
		else:
			max=n3
	elif n2>n3:
		max=n2
	else:
		max=n3
	print("Maximum among",n1,n2,n3,"is ",max)
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
fun(n1,n2,n3)

