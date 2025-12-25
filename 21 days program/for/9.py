pairs = eval(input("Enter list of tuples: "))
result = {}

for key, value in pairs:
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)
