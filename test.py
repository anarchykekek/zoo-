import unittest
from BaseAnimal import *

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.f = BaseAnimal("frog", "www", 10, 5)

    def test_type(self):
        expected = "frog"
        actual = self.f.Type
        self.assertEqual(expected, actual)


    def test_Age(self):
        expected = 10
        actual = self.f.Age
        self.assertEqual(expected, actual)

    def test_IsFeeded(self):
        expected = True
        actual = self.f.IsFeeded()
        self.assertEqual(expected, actual)






if __name__ == "__main__":
    unittest.main()


