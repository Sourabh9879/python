import random

print("you are playing game..")
a = random.randint(1,60)
print(a)

with open("file io/hiscore.txt") as f:
    b = f.read()
    if a > int(b):
        with open("file io/hiscore.txt", "w") as f2:
            f2.write(str(a))
    else:
        print("the number is small")
      
