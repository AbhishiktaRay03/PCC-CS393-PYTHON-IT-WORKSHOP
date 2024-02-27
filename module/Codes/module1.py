import random
max = int(input("Enter maximum length of string: "))
lst = list(range(65,91)) + list(range(97,123))
s = ""
i = random.randint(1,max)
for j in range(i) :
    ch = chr(random.choice(lst))
    s += ch
print("The string is :",s)

l = int(input("Enter the lower limit : "))
u = int(input("Enter the upper limit : "))
val = random.randint(l,u)
print("A random value between",l,"and",u,"is :",val)

val1 = random.randint(0,10) * 7
print("A random multiple of 7 is :",val1)
