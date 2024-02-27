str1=input("Enter the text")
l=str1.split()
i=''
d={"India":"West Bengal"}
l2=[]
for word in l:
	if word in d:
		l2.append(d[word])
	else:
		l2.append(word)
print(" ".join(l2))
		
