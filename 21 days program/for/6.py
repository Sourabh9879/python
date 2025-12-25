data = eval(input("Enter a dictionary: "))
max_key = None
max_value = None

for k in data:
    if max_value is None or data[k] > max_value:
        max_value = data[k]
        max_key = k

print(max_key)
