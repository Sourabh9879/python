def calculate(a, b, op):
    if op == "1":
        return a + b
    if op == "2":
        return a - b
    if op == "3":
        return a * b
    if op == "4":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return None

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")
    if choice == "5":
        print("Exiting calculator.")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Try again.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = calculate(a, b, choice)
    print("Result:", result)
