string = input("Enter the string : ")
text = input("Enter the prefix text : ")
l=string.split(" ")
s=''
for i in l:
  i=text+i
  s=s+' '+i
print('The required string is : ',s)
