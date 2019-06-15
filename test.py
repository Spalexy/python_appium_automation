import unittest

from app import MainClass


class MainClassTest(unittest.TestCase):

    def test_get_local_number(self):
        assert MainClass.get_local_number() == 14, "Функция get_local_number вернула число не равное 14"
