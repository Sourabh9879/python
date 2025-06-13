with open("file io/test.txt") as f:
    a = f.read()
    word = a.replace("donkey" , "####")

with open("file io/test.txt", "w") as f2:
    f2.write(word)  