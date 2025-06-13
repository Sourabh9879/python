a = int(input("Enter a no :"))
b = int(input("Enter a no :"))
c = int(input("Enter a no :"))
d = int(input("Enter a no :"))

if(a>b and a>c and a>d):
    print("A is greater", a)
elif(b>a and b>c and b>d):
    print("B is greater", b)
elif(c>a and c>b and c>d):
    print("C is greater", c)
else:
    print("D is greater", d)