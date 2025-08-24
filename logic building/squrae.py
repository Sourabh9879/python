a = int(input("Enter number from where to start: "))
b = int(input("Enter number to end: "))

def square():
    for i in range(a,b+1):
        print(i*i)

square()