a=int(input("\n Enter a number :"))
f=1
if (a==0 or a==1):
	print("Factorial of",a,"is 1")
elif (a>1):
	for i in range(2,a+1):
		f=f*i
	print("Factorial of",a,"is",f)
else:
	print("Invalid input")
