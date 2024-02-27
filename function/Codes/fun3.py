def fun(s):
	upper=lower=0
	for i in s:
		if i.isupper():
			upper=upper+1
		if i.islower():
			lower=lower+1
	print("Number of uppercase characters: ",upper)
	print("Number of lowercase characters: ",lower)
s=input("Enter the string: ")
fun(s)
