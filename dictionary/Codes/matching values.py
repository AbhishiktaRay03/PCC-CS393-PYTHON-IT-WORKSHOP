dict1={}
dict2={}
unique=[]
fl=0
s=int(input("Enter the number of elements of the dictionary 1:"))
for i in range(0,s):
		key=input("Enter the key:")
		if key not in unique:
				unique.append(key)
		else:
				print("Dictionary doesnot allow duplicate keys")
				exit(0)
		value=input("Enter the corresponding value:")
		dict1[key]=value
unique=[]

s=int(input("Enter the number of elements of the dictionary 2:"))
for i in range(0,s):
		key=input("Enter the key:")
		if key not in unique:
				unique.append(key)
		else:
				print("Dictionary doesnot allow duplicate keys")
				exit(0)
		value=input("Enter the corresponding value:")
		dict2[key]=value
for i in dict1:
		if i in dict2:
				print("Match found ",i,":",dict2[i])
				fl=1
if fl==0:
		print("Key not found")

#merge
for j in dict2:
		if j not in dict1:
				dict1[j]=dict2[j]
print("New dict = ",dict1)
