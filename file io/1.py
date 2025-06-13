with open("file io/poems.txt") as f:
    content = f.read()

if("twinkle" in content):
    print("the word twinkle is present")
else:
    print("the word twinkle is not present")
