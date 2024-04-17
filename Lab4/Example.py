from collections import deque

numbers = deque()

numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

# stack
last_item = numbers.pop()
print(last_item) # 47
print(numbers) # deque([99, 15, 82, 50])

# queue
first_item = numbers.popleft()
print(first_item) # 99
print(numbers) # deque([15, 82, 50])