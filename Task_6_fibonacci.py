# Fibonacci Comparison

# Iterative Fibonacci
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Recursive Fibonacci with call count
call_count = 0

def fib_recursive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Main
num = int(input("Enter number: "))

print("Iterative Fibonacci:", fib_iterative(num))

call_count = 0
print("Recursive Fibonacci:", fib_recursive(num))
print("Number of recursive calls:", call_count)