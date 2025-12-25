data = eval(input("Enter a dictionary: "))
swapped = {}

for k in data:
    swapped[data[k]] = k

print(swapped)
