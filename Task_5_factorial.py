# Factorial using Iteration and Recursion

# Iterative
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Main
num = int(input("Enter number: "))

print("Iterative factorial =", factorial_iterative(num))
print("Recursive factorial =", factorial_recursive(num))