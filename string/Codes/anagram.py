string1 = input("Enter the first string : ")
string2 = input("enter the second string : ")
if sorted(string1)==sorted(string2):
    print("The two strings are anagram")
else:
    print("The two strings are not anagram")
