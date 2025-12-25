n = int(input("Enter a positive integer: "))
counts = [0] * 10

num = n
while num > 0:
    digit = num % 10
    counts[digit] += 1
    num //= 10

print("Digit frequencies for", n)
for digit, freq in enumerate(counts):
    print(f"{digit}: {freq}")
