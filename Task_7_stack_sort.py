# Stack + Selection Sort

# Stack implementation
stack = []

# Push elements
stack.append(30)
stack.append(10)
stack.append(50)
stack.append(20)

print("Stack:", stack)

# Convert to list (already list)
lst = stack.copy()

# Selection Sort
n = len(lst)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if lst[j] < lst[min_index]:
            min_index = j

    lst[i], lst[min_index] = lst[min_index], lst[i]

print("Sorted Stack:", lst)