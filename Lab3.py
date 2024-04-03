class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.item)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            new_node = Node(item)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def pop(self):
        if self.head is None:
            return None
        else:
            item = self.tail.item
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return item


class Text:
    def __init__(self, text):
        # self.text = text
        self.words = text.lower().split()

"""9. Кожне слово тексту, що починається на задану літеру, написати з
заголовної літери. До всіх слів з непарною кількістю літер дописати знак
оклику."""

text = Text(input('Enter text: '))



# tst = DoublyLinkedList()
# tst.push(1)
# tst.push(2)
# tst.push(3)
# tst.push(4)
# tst.push(5)
# tst.push(6)
# tst.push(7)
# tst.push(8)
# tst.push(9)
# tst.push(10)
# print(tst.pop())
# print(tst.pop())
# print(tst.pop())
# print(tst.pop())
# print(tst.head, tst.tail, tst.head.next, tst.tail.prev, tst.head.prev, tst.tail.next)