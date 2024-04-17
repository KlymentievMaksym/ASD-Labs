# На максимальний бал реалізувати чергу двома способами: масивом (використовувати кільцеву чергу , див. лекцію) та зв'язним списком.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            item = self.head.data
            self.head = self.head.next
            return item

    def __iter__(self):
        node = self.head
        while node:
            yield str(node)
            node = node.next

    def __str__(self):
        return ' '.join(self)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(0)
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.pop()
    linked_list.push(4)
    linked_list.push(5)
    print(linked_list)
