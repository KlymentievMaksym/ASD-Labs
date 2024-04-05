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
        self.size = 0

    def push(self, item):
        if self.head is None:
            self.head = Node(item)
            self.size += 1
            self.tail = self.head
            # self.head.prev = self.tail
            # self.tail.next = self.head
        else:
            new_node = Node(item)
            self.size += 1
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            # self.tail.next = self.head
            # self.head.prev = self.tail

    def pop(self):
        if self.head is None:
            # return None
            raise IndexError("Linked List is empty")
        else:
            item = self.tail.item
            if self.head == self.tail:
                self.head = None
                self.tail = None
                # self.size = 0
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.size -= 1
            return item
    
    def pop_by_index(self, index:int):
        if index == -1:
            index = self.size-1
        if self.head is None:
            raise IndexError("Linked List is empty")
        elif index > self.size-1:
            raise IndexError("Index out of range")
        else:
            # print(index, self.size)
            if index == 0:
                item = self.head.item
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                self.size -= 1
                return item
            elif index == self.size-1:
                item = self.tail.item
                self.tail = self.tail.prev
                self.tail.next = None
                self.size -= 1
                return item
            else:
                node = self.head
                for _ in range(index):
                    node = node.next
                item = node.item
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                return item
    
    def insert(self, index:int, item):
        if index > self.size:
            raise IndexError("Index out of range")
        else:
            new_node = Node(item)
            if index == 0:
                # print("HEAD")
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                # print(self.head, self.head.next)
            elif index == self.size:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                # print(self.tail.prev, self.tail)
            else:
                # print("MIDDLE")
                node = self.head
                for _ in range(index-1):
                    node = node.next
                # print(node.prev, node, node.next)
                # print(new_node)
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                new_node.next.prev = new_node
                # print(new_node.prev, new_node, new_node.next)
            self.size += 1
            
    
    def __iter__(self):
        node = self.head
        while node:
            # print(str(node))
            yield str(node)
            node = node.next


class Text:
    def __init__(self, text:str, list_type=list):
        if type(text) != str:
            raise TypeError("Text must be a string")
        self.type = list_type
        if self.type is list:
            if text != "" and text[-1] != ".":
                raise ValueError("Text must end with a dot")
            self.words = text.lower().split()
        else:
            if text != "" and text[-1] != ".":
                raise ValueError("Text must end with a dot")
            self.words = DoublyLinkedList()
            self.text = text
    
    def start(self, char:str):
        self.char = char.lower()
        if self.type is list:
            for word in self.words:
                if word[0] == self.char:
                    self.words[self.words.index(word)] = self.char.capitalize() + word[1:]
                    word = self.char.capitalize() + word[1:]
                if len(word) % 2 == 1:
                    index = self.words.index(word)
                    self.words[index] = self.words[index] + "!"
        else:
            # print("I WAS CALLED")
            # print(len(self.text))
            word = ''
            for letter_index in range(len(self.text)):
                letter = self.text[letter_index]
                if letter != ' ':
                    # print("I AM MAKING WORD")
                    if letter_index > 0 and self.text[letter_index-1] == " " and self.text[letter_index] == self.char:
                        word += self.char.capitalize()
                    else:
                        word += letter
                    # print(word)
                else:
                    if len(word) % 2 == 1:
                        word += "!"
                    # print("I AM PUSHING")
                    # print(word)
                    self.words.push(word)
                    word = ''
            if word != '' and word[-1] == '.':
                if len(word) % 2 == 1:
                        word += "!"
                self.words.push(word)
            # print("I AM DONE PUSHING")

    def insert(self, index:int, word:str):
        if self.type is list and index > len(self.words):
            raise IndexError("Index out of range")
        if index != -1:
            if self.type is not list and word[0].lower() == self.char:
                word = self.char.capitalize() + word[1:]
            if self.type is not list and len(word) % 2 == 1:
                word += "!"
            self.words.insert(index, word)
            # print(self.words)
        else:
            if self.type is list:
                self.words.insert(len(self.words), word)
            else:
                self.words.insert(self.words.size, word)
    
    def remove_by_index(self, index:int):
        try:
            if self.type is list:
                self.words.pop(index)
                if self.words == []:
                    print("Text is empty")
            else:
                self.words.pop_by_index(index)
                if self.words.head is None:
                    print("Text is empty")
        except IndexError:
            raise IndexError("Index out of range")
    
    def __str__(self) -> str:
        # if self.type is list:
        return ' '.join(self.words)
        # else:
        #     return ""

if __name__ == '__main__':
    text = Text(input("Enter text: "))
    text.upper_case(input("Enter letter to capitalise in start of words: "))
    print(text)

"""9. Кожне слово тексту, що починається на задану літеру, написати з
заголовної літери. До всіх слів з непарною кількістю літер дописати знак
оклику.

Слова тексту із малих латинських літер записані не менше, ніж через
один пробіл; текст закінчується крапкою. Написати програму введення
такого тексту з клавіатури та його обробки, використовуючи: а) масив та  б)
список. Виконати завдання відповідно до свого варіанту.

Загальний алгоритм розв’язання поставленої задачі, як правило, не
залежить від конкретної реалізації структури даних. Але всі дії над текстом
(пошук слів, виділення будь-якого із слів, перестановка літер в слові тощо)
повинні бути описані функціями,  «налаштованими» на конкретну реалізацію
з допомогою формальних параметрів.

Інтерфейс програми має бути зрозумілим непідготовленому
користувачеві. При розробці інтерфейсу програми слід передбачити:
 задання формату і діапазону даних, що вводяться;
 блокування введення невірних за типом і форматом даних;
 задання операції, яка виконується програмою;
 наявність пояснень при виведенні результату.
Потрібно також вивести на екран інформацію про час виконання
програми при використанні масиву і списку та про об’єм пам’яті, необхідний
у кожному з цих випадків.
При тестуванні програми необхідно:
 перевірити правильність введення та виведення даних (зокрема,
відстежити спроби введення даних, неправильних за типом і
форматом);
 забезпечити виведення повідомлень за відсутності вхідних даних
(«пусте введення»);
 перевірити правильність виконання операцій, зокрема, при повністю
заповненому масиві;
 відстежити вихід за межі масиву;
 забезпечити виведення відповідних повідомлень при спробі
видалення елемента з пустого списку або масиву;
 відстежити переповнення масиву.
При представленні тексту у вигляді списку необхідно:
 перевірити можливість вставки елемента в початок, в кінець і в
середину списку;
 проконтролювати правильність видалення елемента з кінця,
середини, початку списку;
 відстежити видалення єдиного елемента і видалення елемента з
порожнього списку;
 перевірити, як звільняється пам’ять при видаленні елемента зі
списку.
"""