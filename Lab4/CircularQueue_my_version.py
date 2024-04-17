# На максимальний бал реалізувати чергу двома способами: масивом (використовувати кільцеву чергу , див. лекцію) та зв'язним списком.
class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def __str__(self):
        return str(self.data)


class CircularQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.index = 0
        self.size = 0

    def get_strqueue(self):
        strqueue = []
        for node in self.queue:
            strqueue += [str(node)]
        return strqueue

    def add(enqueue):
        def check(*args, **kwargs):
            strqueue = args[0].get_strqueue()
            data = enqueue(*args)
            if "print" in kwargs and kwargs["print"]:
                print(f"Added {data} with key {data.key} to queue {strqueue}")
        return check

    def remove(dequeue):
        def check(*args, **kwargs):
            strqueue = args[0].get_strqueue()
            pop = dequeue(*args)
            if "print" in kwargs and kwargs["print"]:
                print(f"Removed {pop} with key {pop.key} from queue {strqueue}")
        return check

    @add
    def enqueue(self, data):
        if self.size < self.capacity:
            data = Node(data, self.size)
            self.queue += [data]
            self.size += 1
            self.index = 0
        else:
            print("Queue is full, overwriting...")
            data = Node(data, self.index)
            self.queue[self.index] = data
            self.index += 1
        return data

    @remove
    def dequeue(self):
        self.size -= 1
        pop = self.queue.pop(0)
        for node in self.queue:
            node.key -= 1
        return pop

    def __str__(self):
        return f"\nhead: |{self.queue[0].data}|, key: |{self.queue[0].key}|\n[" + ", ".join(self.get_strqueue()) + f"]\ntail: |{self.queue[-1].data}|, key: |{self.queue[-1].key}|\n"

if __name__ == "__main__":
    que = CircularQueue(5)
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    print(que)
    que.enqueue(7, print=True)
    que.enqueue(7, print=True)
    print(que)
    que.dequeue(print=True)
    print(que)
    que.enqueue(6, print=True)
    print(que)
    que.dequeue(print=True)
    print(que)
    que.dequeue(print=True)
    print(que)
    que.dequeue(print=True)
    print(que)
