l = list(map(int, input('Enter the numbers in the list(separated by spaces) : ').split()))
res=[]
print('The list input by the user is : ',l)

for i in l:
	t=(i,i**3)
	res.append(t)

print('The resultant list is : ',res)

