import math

r=float(input("Enter the radius of the cylinder : "))
h=float(input("Enter the height of the cylinder : "))

v=math.pi*r*r*h

choice=int(input('Enter 1 for open cylinder\nEnter 2 for closed cylinder: '))

if choice==1:
	s=2*math.pi*r*h
else:
	s=2*math.pi*r*h + 2*math.pi*r*r
	
print("Volume is: ",v)
print("Surface Area is: ",s)

