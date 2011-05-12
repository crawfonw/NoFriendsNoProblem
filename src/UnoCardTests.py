import unittest
from UnoCardObjects import UnoCard

class TestUnoCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_to_string_number(self):
        c = UnoCard(1, "Number", "Red")
        self.assertEqual(str(c), "Red 1")

    def test_to_string_wild_card(self):
        c = UnoCard(-1, "Wild", "Black")
        self.assertEqual(str(c), "Wild Card")

    def test_to_string_other_card(self):
        c = UnoCard(-1, "Skip", "Green")
        self.assertEqual(str(c), "Green Skip")

    def test_invalid_color(self):
        self.assertRaises(ValueError, UnoCard, 2, "Number", "Cyan")

    def test_invalid_type(self):
        self.assertRaises(ValueError, UnoCard, 2, "Bunneh", "Red")

    def test_invalid_number(self):
        self.assertRaises(ValueError, UnoCard, 14, "Hearts")

if __name__ == '__main__':
    unittest.main()

