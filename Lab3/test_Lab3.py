import unittest
import Lab3
import sys

class Tests(unittest.TestCase):
    def test_standart(self):
        text = Lab3.Text("[your, computer] has a viruss.")
        text.start("a")
        text1 = Lab3.Text("[your, computer] has a viruss.", Lab3.DoublyLinkedList)
        text1.start("a")
        self.assertEqual(str(text), "[your, computer]! has! A! viruss.!")
        self.assertEqual(str(text1), "[your, computer]! has! A! viruss.!")
    
    def test_without_dot(self):
        with self.assertRaises(ValueError):
            Lab3.Text("hello")
        with self.assertRaises(ValueError):
            Lab3.Text("hello", Lab3.DoublyLinkedList)
    
    def test_empty(self):
        text = Lab3.Text("")
        text.start("")
        text1 = Lab3.Text("", Lab3.DoublyLinkedList)
        text1.start("")
        self.assertEqual(str(text), "")
        self.assertEqual(str(text1), "")
    
    def test_another_types(self):
        with self.assertRaises(TypeError):
            Lab3.Text(123)
        with self.assertRaises(TypeError):
            Lab3.Text(['hello', 'world'])
        with self.assertRaises(TypeError):
            Lab3.Text(123, Lab3.DoublyLinkedList)
        with self.assertRaises(TypeError):
            Lab3.Text(['hello', 'world'], Lab3.DoublyLinkedList)
        
    def test_pop(self):
        text = Lab3.Text("hello.")
        text.words.pop()
        text1 = Lab3.Text("hello.", Lab3.DoublyLinkedList)
        text1.start("")
        text1.words.pop()
        with self.assertRaises(IndexError):
            text.words.pop()
        with self.assertRaises(IndexError):
            text1.words.pop()
    
    def test_insert(self):
        text = Lab3.Text("hello.")
        text.insert(0, "hi")
        text.insert(-1, "Dad.")
        text.insert(len(text.words)//2, "middle")
        text.start("")
        text1 = Lab3.Text("hello.", Lab3.DoublyLinkedList)
        text1.start("")
        text1.insert(0, "hi")
        text1.insert(-1, "Dad.")
        text1.insert(text1.words.size//2, "middle")
        self.assertEqual(str(text), "hi middle hello. Dad.")
        self.assertEqual(str(text1), "hi middle hello. Dad.")

    def test_remove(self):
        text = Lab3.Text("hi middle hello! Dad.")
        text.remove_by_index(0)
        text.remove_by_index(-1)
        text.remove_by_index(len(text.words)//2)
        text.start("")
        text1 = Lab3.Text("hi middle hello! Dad.", Lab3.DoublyLinkedList)
        text1.start("")
        text1.remove_by_index(0)
        text1.remove_by_index(-1)
        text1.remove_by_index(text1.words.size//2)
        self.assertEqual(str(text), "middle")
        self.assertEqual(str(text1), "middle")
    
    def test_remove_from_one_and_empty(self):
        text = Lab3.Text("Helo.")
        text.remove_by_index(0)
        text1 = Lab3.Text("Helo.", Lab3.DoublyLinkedList)
        text1.start("")
        text1.remove_by_index(0)
        with self.assertRaises(IndexError):
            text.remove_by_index(0)
        with self.assertRaises(IndexError):
            text1.remove_by_index(0)
    
    def test_insert_wrong_index(self):
        text = Lab3.Text("hello.")
        text1 = Lab3.Text("hello.", Lab3.DoublyLinkedList)
        text1.start("")
        with self.assertRaises(IndexError):
            text.insert(len(text.words)+1, "hi")
        with self.assertRaises(IndexError):
            text1.insert(text1.words.size+1, "hi")
    
    def test_remove_wrong_index(self):
        text = Lab3.Text("hello.")
        text1 = Lab3.Text("hello.", Lab3.DoublyLinkedList)
        text1.start("")
        with self.assertRaises(IndexError):
            text.remove_by_index(1)
        with self.assertRaises(IndexError):
            text1.remove_by_index(1)
        
    def test_memory_usage(self):
        text = Lab3.Text("hello dad.")
        size = sys.getsizeof(text.words)
        text.remove_by_index(0)
        text1 = Lab3.Text("hello dad.", Lab3.DoublyLinkedList)
        text1.start("")
        size1 = sys.getsizeof(text1.words)
        text1.remove_by_index(0)
        self.assertGreaterEqual(size, sys.getsizeof(text.words))    
        self.assertGreaterEqual(size1, sys.getsizeof(text1.words))

    
"""
При тестуванні програми необхідно:
 перевірити правильність введення та виведення даних (зокрема,
відстежити спроби введення даних, неправильних за типом і
форматом); +
 забезпечити виведення повідомлень за відсутності вхідних даних
(«пусте введення»); +
 перевірити правильність виконання операцій, зокрема, при повністю
заповненому масиві; -
 відстежити вихід за межі масиву; +
 забезпечити виведення відповідних повідомлень при спробі
видалення елемента з пустого списку або масиву; +
 відстежити переповнення масиву. +

При представленні тексту у вигляді списку необхідно:
 перевірити можливість вставки елемента в початок, в кінець і в
середину списку; +
 проконтролювати правильність видалення елемента з кінця,
середини, початку списку; +
 відстежити видалення єдиного елемента і видалення елемента з
порожнього списку; +
 перевірити, як звільняється пам’ять при видаленні елемента зі
списку. +
"""
    
if __name__ == '__main__':
    unittest.main()