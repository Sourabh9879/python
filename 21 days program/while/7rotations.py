n = input("Enter a number: ").strip()
original = n
rotated = n
count = 0

if len(n) == 0:
    print("No number entered.")
else:
    while True:
        rotated = rotated[-1] + rotated[:-1]
        count += 1
        if rotated == original:
            break
    print("Rotations needed to return:", count)
