import random

computer = random.choice([-1, 0, 1])

youDict = { "s" : 1, "w" : 0, "g" : -1}
reversedDict = { 1 : "Snake", 0 : "Water", -1 : "Gun"}
num = input("Enter your choice ( s, w, g) :")
yourNum = youDict[num]
print(f"You Chose {reversedDict[yourNum]} \nComputer Chose {reversedDict[computer]}")

if(computer == yourNum):
    print("its a draw")
else:
    if(computer == 1 and yourNum == -1):
        print("You Win!")
    elif(computer == 1 and yourNum == 0):
        print("You Lose!")
    elif(computer == 0 and yourNum == -1):
        print("You Lose!")
    elif(computer == 0 and yourNum == 1):
        print("You Win!")
    elif(computer == -1 and yourNum == 1):
        print("You Lose!")
    elif(computer == -1 and yourNum == 0):
        print("You Win!")
    else:
        print("Something Went Wrong")