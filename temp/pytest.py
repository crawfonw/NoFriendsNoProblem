import random
import unittest


class AllFunctions():

    def __init__(self):
        pass

    def multiply(self, a, b):
        return a * b

class Tests(unittest.TestCase):

    def setUp(self):
        self.funcs = AllFunctions()

    def test_muliply(self):
        self.assertEqual(self.funcs.multiply(4,5), 20)

if __name__ == '__main__':
    unittest.main()

