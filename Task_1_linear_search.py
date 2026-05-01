# Linear Search Program

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i + 1   # position (1-based)
    return -1

# Main
lst = [10, 20, 30, 40, 50]
print("List:", lst)

target = int(input("Enter element to search: "))

result = linear_search(lst, target)

if result != -1:
    print("Element found at position", result)
else:
    print("Element not found")