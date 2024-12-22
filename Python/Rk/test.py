import main
import unittest

class ClassTest(unittest.TestCase):
    def test_first(self):
        test_list_1 = [main.Book(1, "Документ о книга"), main.Book(2, "Библиотека"), main.Book(3, "Наука")]
        test_list_2 = [main.Chapter(1, 'Глава 1', 25000, 1), main.Chapter(2, 'Глава 2', 35000, 2), main.Chapter(3, 'КГлава 3', 45000, 3)]
        result = main.first_task(test_list_1,test_list_2)
        expected = [('Глава 1', 25000, 'Документ о книга')]
        #print(result)
        self.assertEqual(result, expected)

        
    def test_second(self):
        test_list_1 = [main.Book(1, "Документ о книга"), main.Book(2, "Библиотека"), main.Book(3, "Наука")]
        test_list_2 = [main.Chapter(1, 'Глава 1', 25000, 1), main.Chapter(2, 'Глава 2', 35000, 2), main.Chapter(3, 'КГлава 3', 45000, 3)]

        result = main.second_task(test_list_1,test_list_2)
        expected = [('Наука', 45000.0), ('Библиотека', 35000.0), ('Документ о книга', 25000.0)]
        #print(result)
        self.assertEqual(result, expected)

    def test_third(self):
        test_list = [("Кдосуг", 5, "Книга"), ("КЗемля", 3, "Книга"), ("Что-то", 2, "Что-то книга")]
        result = main.third_task(test_list)
        expected = [('Кдосуг', 'Книга'), ('КЗемля', 'Книга')]
        #print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()