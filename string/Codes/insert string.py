string = input("Enter a string : ")
string2 = input("Enter the string that is to be inserted : ")
length = len(string)//2
print(string[:length]+' '+string2+' '+string[length:])
