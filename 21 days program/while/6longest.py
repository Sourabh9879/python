longest = 0
current = 0
prev = None

while True:
    value = int(input("Enter number (-1 to stop): "))
    if value == -1:
        break

    if prev is None or value > prev:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

    prev = value

print("Longest increasing run length:", longest)
