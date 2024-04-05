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
            # self.head.prev = self.tail
            # self.tail.next = self.head
        else:
            new_node = Node(item)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            # self.tail.next = self.head
            # self.head.prev = self.tail

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
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Text:
    def __init__(self, text:str):
        if type(text) != str:
            raise TypeError("Text must be a string")
        self.words = text.lower().split()
    
    def upper_case(self, char:str):
        char = char.lower()
        for word in self.words:
            if word[0] == char:
                self.words[self.words.index(word)] = char.capitalize() + word[1:]
        self.find_and_replace_odd_length_words()
    
    def find_and_replace_odd_length_words(self):
        for word in self.words:
            if len(word) % 2 == 1:
                self.words[self.words.index(word)] = self.words[self.words.index(word)] + "!"
    
    def insert(self, index:int, word:str):
        if index > len(self.words):
            raise IndexError("Index out of range")
        if index != -1:
            self.words.insert(index, word)
            # print(self.words)
        else:
            self.words.insert(len(self.words), word)
    
    def remove_by_index(self, index:int):
        try:
            self.words.pop(index)
            if self.words == []:
                print("Text is empty")
        except IndexError:
            raise IndexError("Index out of range")
    
    def __str__(self) -> str:
        return ' '.join(self.words)

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