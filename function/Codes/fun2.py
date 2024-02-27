def fun(l):
	mul=1
	for i in l:
		mul=mul*i
	print("Multiplication of all the numbers in the list are :",mul)
l=list(map(int,input("Enter the numbers in a list seperated by spaces").split()))
fun(l)
