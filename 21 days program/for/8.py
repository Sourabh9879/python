items = input("Enter list items (space-separated): ").split()
pairs = []

for i in range(len(items)):
    for j in range(len(items)):
        if i != j:
            pairs.append((items[i], items[j]))

print(pairs)
