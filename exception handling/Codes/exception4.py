try :
	with open("data.txt","r") as file :
		content = file.read()
		print("Content of the file, 'data.txt' : ")
		print(content)
except Exception as e :
	print("ERROR :",e)
