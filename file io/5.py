list = ["donkey" , "bad", "gadha"]

with open("file io/test.txt") as file:
    word = file.read()

for data in list:
    word = word.replace(data, "####")

with open("file io/test.txt", "w") as file:
    file.write(word)
