numbers = []

while True:
    value = int(input("Enter an integer (palindrome ends): "))

    # reverse without converting to string
    original = value
    rev = 0
    temp = value
    if temp < 0:
        temp = -temp
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    if value < 0:
        rev = -rev

    if value == rev:
        print("Palindrome found, stopping.")
        break

    numbers.append(value)

print("Numbers entered before palindrome:", numbers)
