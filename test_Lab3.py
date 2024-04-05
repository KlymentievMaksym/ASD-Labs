import unittest
import Lab3
import sys

class Tests(unittest.TestCase):
    def test_standart(self):
        text = Lab3.Text("[your, computer] has a viruss.")
        text.upper_case("a")
        self.assertEqual(str(text), "[your, computer]! has! A! viruss.!")
    
    def test_empty(self):
        text = Lab3.Text("")
        text.upper_case("")
        self.assertEqual(str(text), "")
    
    def test_another_types(self):
        with self.assertRaises(TypeError):
            Lab3.Text(123)
        with self.assertRaises(TypeError):
            Lab3.Text(['hello', 'world'])
        
    def test_pop(self):
        text = Lab3.Text("hello")
        text.words.pop()
        with self.assertRaises(IndexError):
            text.words.pop()
    
    def test_insert(self):
        text = Lab3.Text("hello")
        text.insert(0, "hi")
        text.insert(-1, "Dad.")
        text.insert(len(text.words)//2, "middle")
        text.upper_case("")
        self.assertEqual(str(text), "hi middle hello! Dad.")

    def test_remove(self):
        text = Lab3.Text("hi middle hello! Dad.")
        text.remove_by_index(0)
        text.remove_by_index(-1)
        text.remove_by_index(len(text.words)//2)
        text.upper_case("")
        self.assertEqual(str(text), "middle")
    
    def test_remove_from_empty(self):
        text = Lab3.Text("Helo")
        text.remove_by_index(0)
        with self.assertRaises(IndexError):
            text.remove_by_index(0)
    
    def test_insert_wrong_index(self):
        text = Lab3.Text("hello")
        with self.assertRaises(IndexError):
            text.insert(len(text.words)+1, "hi")
    
    def test_remove_wrong_index(self):
        text = Lab3.Text("hello")
        with self.assertRaises(IndexError):
            text.remove_by_index(1)

    def test_memory_usage(self):
        text = Lab3.Text("hello dad.")
        size = sys.getsizeof(text.words)
        text.remove_by_index(0)
        self.assertGreater(size, sys.getsizeof(text.words))        

    
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