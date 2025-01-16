# 1. Перевірка функції піднесення до квадрату

# • Напишіть функцію square(num), яка повертає квадрат числа.
# • Створіть тести для перевірки:
# o Додатних і від'ємних чисел.
# o Нуля.

import unittest

def square(num):
    return num ** 2

class TestsVerification(unittest.TestCase):

    def test_positive(self):                  # тест для перевірки: Додатних
        self.assertEqual(square(2),4)

    def test_negative(self):                  # тест для перевірки: Від'ємних
        self.assertEqual(square(-2),4)

    def test_zero(self):                      # тест для перевірки: Нуля
        self.assertEqual(square(0),0)





