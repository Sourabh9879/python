words = input("Enter words (space-separated): ").split()
groups = {}

for w in words:
    if not w:
        continue
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)

print(groups)
