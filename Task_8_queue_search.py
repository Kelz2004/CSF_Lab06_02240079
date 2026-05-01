# Queue + Linear Search

from collections import deque

# Queue implementation
queue = deque()

# Insert elements
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue:", list(queue))

# Linear search
target = int(input("Enter element to search: "))

found = False
position = 1

for item in queue:
    if item == target:
        found = True
        break
    position += 1

if found:
    print("Element found at position", position)
else:
    print("Element not found")