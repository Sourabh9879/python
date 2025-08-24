def reverse_pyramid(n):
    for i in range(n, 0, -1):  # Start from n, go down to 1
        for k in range(n - i):  # Print leading spaces
            print(" ", end="")
        for j in range(2 * i - 1):  # Print stars
            print("*", end="")
        print()  # Move to the next line

reverse_pyramid(5)