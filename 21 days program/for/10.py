set1 = set(eval(input("Enter first set: ")))
set2 = set(eval(input("Enter second set: ")))
intersection = set()

for x in set1:
    if x in set2:
        intersection.add(x)

print(intersection)
