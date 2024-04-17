from collections import deque
""" From documentation:
Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 
Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
"""

numbers = deque(maxlen=3)

numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

print(numbers)  # deque([82, 50, 47], maxlen=3)

# stack
last_item = numbers.pop()
print(last_item)  # 47
print(numbers)  # deque([82, 50], maxlen=3)

# queue
numbers.append(47)
first_item = numbers.popleft()
print(first_item)  # 82
print(numbers)  # deque([50, 47], maxlen=3)

numbers.appendleft(47)
print(numbers)  # deque([47, 50, 47], maxlen=3)
