with open("file io/data.txt") as f:
    data = f.readline()

if("python" in data):
    print("python is there in txt file")
else:
    print("python is not there in txt file")