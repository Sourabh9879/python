import random

rdmnum = random.randint(1,10)
print(rdmnum)
num = int(input("Guess a Number between 1 and 10 :"))
count = 0

if(rdmnum == num):
    count += 1
    print(f"You have Guessed correct Number in {count} attempt")
elif(rdmnum > num):
    count += 1
    print("Higher Number Please")
elif(rdmnum < num):
    count += 1
    print("Lower Number Please")
else:
    print("Something went wrong")
