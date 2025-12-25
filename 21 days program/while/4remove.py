n = int(input("Enter a number: "))
d = int(input("Enter digit to remove (0-9): "))

# First build the reversed result without the digit
rev_result = 0
num = abs(n)
while num > 0:
    digit = num % 10
    if digit != d:
        rev_result = rev_result * 10 + digit
    num //= 10

# Now reverse again to restore original order
result = 0
if rev_result == 0:
    result = 0
else:
    while rev_result > 0:
        result = result * 10 + rev_result % 10
        rev_result //= 10

# Re-apply sign if needed
if n < 0:
    result = -result

print("Result after removing", d, "is", result)
