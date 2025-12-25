n = int(input("Enter a positive integer: "))
steps = 0

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1

print("Steps to reach 1:", steps)
