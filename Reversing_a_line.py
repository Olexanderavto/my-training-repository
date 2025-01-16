# 2. Реверсування рядка

# • Реалізуйте функцію reverse_string(s), яка повертає реверсований рядок.
# • Напишіть тести для:
# o Порожнього рядка.
# o Рядка з одним символом.
# o Довгого рядка.

import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseStringFunction(unittest.TestCase):

    def test_empty_line(self):
        self.assertEqual(reverse_string(""), "")      # тест для перевірки: Порожнього рядка


    def test_single_character_string(self):                       # тест для перевірки: Рядка з одним символом
        self.assertEqual(reverse_string("m"), "m")

    def test_long_line(self):
        self.assertEqual(reverse_string("main.py"), "yp.niam")
