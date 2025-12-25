data = tuple(input("Enter tuple items (space-separated): ").split())
seen = set()
all_unique = True

for x in data:
    if x in seen:
        all_unique = False
        break
    seen.add(x)

print(all_unique)
