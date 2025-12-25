list1 = list(map(int, input("Enter first list (space-separated): ").split()))
list2 = list(map(int, input("Enter second list (space-separated): ").split()))
common = []

for x in list1:
    found = False
    for y in list2:
        if x == y:
            found = True
            break
    if found and x not in common:
        common.append(x)

print(common)
