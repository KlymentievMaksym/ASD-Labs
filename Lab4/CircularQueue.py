# На максимальний бал реалізувати чергу двома способами: масивом (використовувати кільцеву чергу , див. лекцію) та зв'язним списком.
class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def __str__(self):
        return str(self.data)


class Q:
    def __init__(self, capacity):
        self.head = 0
        self.tail = 0
        self.length = capacity
        self.queue = [Node(None, -1)] * self.length

    def lower_key(self):
        for node in self.queue:
            if node.key > 0:
                node.key -= 1

    def find_index_by_key(self, key):
        for index in range(len(self.queue)):
            if self.queue[index].key == key:
                return index

    def check_for_nones(self):
        for node in self.queue:
            if node.key == -1:
                return True
        return False

    def find_awailable_key(self):
        keys = [i for i in range(self.length)]
        key = -1
        for node in self.queue:
            if node.key > key:
                key = node.key
            if node.key in keys:
                keys.remove(node.key)
        if key in keys:
            return key + 1
        elif keys == []:
            print("No key available")
            return -2
        else:
            return keys[0]

    def Enqueue(self, x, **kwargs):
        x = Node(x, self.find_awailable_key())
        if self.tail == self.length:
            if len(self.queue) == self.length and not self.check_for_nones():
                print("Queue is full")
                if "overwrite" in kwargs and kwargs["overwrite"]:
                    self.tail = self.tail % self.length
                    self.queue[self.tail] = x
                    self.lower_key()
                    if self.queue[self.tail].key == -2:
                        self.queue[self.tail].key = self.find_awailable_key()
                    self.tail += 1
            else:
                self.tail = self.tail % self.length
                self.queue[self.tail] = x
                self.tail += 1
        else:
            if not self.check_for_nones():
                print("Queue is full")
                if "overwrite" in kwargs and kwargs["overwrite"]:
                    self.lower_key()
                    if x.key == -2:
                        x.key = self.find_awailable_key()
                        self.queue[self.tail] = x
            else:
                self.queue[self.tail] = x
            self.tail += 1
        if "print" in kwargs and kwargs["print"]:
            print(self)

    def Dequeue(self, **kwargs):
        x = self.queue[self.find_index_by_key(0)]
        self.queue[self.find_index_by_key(0)] = Node(None, -1)
        self.lower_key()
        if "print" in kwargs and kwargs["print"]:
            print(self)
        return x

    def __str__(self) -> str:
        strqueue = []
        for node in self.queue:
            strqueue += [[node.data, f"k: {node.key}"]]
        return str(strqueue)


if __name__ == '__main__':
    print("----------Without overwrite----------")
    q = Q(5)
    q.Enqueue(1)
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(2, print=True)
    q.Enqueue(3, print=True)
    q.Enqueue(4, print=True)
    q.Enqueue(5, print=True)
    q.Dequeue(print=True)
    q.Dequeue(print=True)
    q.Enqueue(7)
    q.Enqueue(9)
    q.Enqueue(11, print=True)
    print()
    print()
    print("----------With overwrite----------")
    q = Q(5)
    q.Enqueue(1)
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(2, print=True)
    q.Enqueue(3, print=True)
    q.Enqueue(4, overwrite=True, print=True)
    q.Enqueue(5, overwrite=True, print=True)
    q.Dequeue(print=True)
    q.Dequeue(print=True)
    q.Enqueue(7)
    q.Enqueue(9, print=True)
    q.Enqueue(11, overwrite=True, print=True)
