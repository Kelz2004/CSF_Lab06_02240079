# Indexed (Block) Search

import math

def indexed_search(lst, target):
    n = len(lst)
    block_size = int(math.sqrt(n))
    start = 0
    end = block_size

    # Finding block
    while start < n and lst[min(end, n) - 1] < target:
        start = end
        end += block_size
        if start >= n:
            return False

    # Linear search within block
    for i in range(start, min(end, n)):
        if lst[i] == target:
            return True

    return False

# Main
lst = [5, 10, 15, 20, 25, 30]
print("List:", lst)

target = int(input("Enter element: "))

if indexed_search(lst, target):
    print("Element found")
else:
    print("Element not found")