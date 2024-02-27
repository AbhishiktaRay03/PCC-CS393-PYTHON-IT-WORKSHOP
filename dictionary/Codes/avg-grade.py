dict={}
unique=[]
value=[]
grade=''
dict["name"]=input("Enter the name of student ")
dict["assignment"]=list(map(float,input('Enter the assignment marks with spaces: ').split()))
dict["test"]=list(map(float,input('Enter the test marks with spaces: ').split()))
dict["lab"]=list(map(float,input('Enter the lab marks with spaces: ').split()))
avg = (0.1* (sum(dict["assignment"])/len(dict["assignment"]))) + (0.7* (sum(dict["test"])/len(dict["test"]))) + (0.2* (sum(dict["lab"])/len(dict["lab"])))

if avg>=90:
		grade='A'
elif avg>=80:
		grade='B'
elif avg>=70:
		grade='C'
elif avg>=60:
		grade='D'
else:
		grade='F'
		
print('Average marks of',dict["name"],'is',avg)
print('Letter grade of',dict["name"],'is',grade)

