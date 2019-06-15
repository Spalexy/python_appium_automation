import unittest

from app import MainClass


class MainClassTest(unittest.TestCase):

    def test_get_local_number(self):
        assert MainClass.get_local_number() == 14, "Функция get_local_number вернула число не равное 14"

    def test_get_class_number(self):
        assert MainClass.get_class_number(MainClass) > 45, "Номер тестируемого класса <= 45"
