myList = ["apple", "banana", "cherry",25,56,True,0]
print(myList)

if "apple" in myList:
    print("Apple is present in list")

myList[1] = "grapes"
myList.append("mango")
myList.remove(True)
print(myList)