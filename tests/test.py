import unittest

from appium import webdriver
from app import MainClass


class MainClassTest(unittest.TestCase):

    def test_get_local_number(self):
        assert MainClass().get_local_number() == 14, 'Функция get_local_number вернула число не равное 14'

    def test_get_class_number(self):
        MainClass()
        assert MainClass().get_class_number() > 45, 'Номер тестируемого класса <= 45'

    def test_get_class_string(self):
        class_str = MainClass().get_class_string()
        assert any(s in class_str for s in ['Hello', 'hello']), 'Строка класса не содержит ключевого слова'
