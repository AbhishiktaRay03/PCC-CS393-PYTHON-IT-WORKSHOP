dict={}
i=0
j=''
unique=[]
s=int(input("Enter the number of elements of the dictionary:"))
for i in range(0,s):
		key=input("Enter the key:")
		if key not in unique:
				unique.append(key)
		else:
				print("Dictionary doesnot allow duplicate keys")
				exit(0)
		value=input("Enter the corresponding value:")
		dict[key]=value

key_list1=list(dict.keys())
#logic of value sort
val_list=list(dict.values())

test={val_list[i]:key_list1[i] for i in range(0,s)}
val_list=list(test.keys())
val_list.sort()
valdict={test[j]:j for j in val_list}

#logic of key sort
key_list1.sort()
keydict={i:dict[i] for i in key_list1}
print("Sorting according to keys:")
print(keydict)
print("Sorting according to values:")
print(valdict)

