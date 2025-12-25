items = input("Enter list items (space-separated): ").split()
k = int(input("Enter k: "))
rotated = []

if items:
    k = k % len(items)
    for i in range(len(items)):
        rotated.append(items[(i + k) % len(items)])

print(rotated)
