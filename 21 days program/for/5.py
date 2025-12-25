items = input("Enter list items (space-separated): ").split()
unique = []

for x in items:
    if x not in unique:
        unique.append(x)

print(unique)
