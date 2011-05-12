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

    def test_valid_set_color_of_wild(self):
        c = UnoCard(-1, "Wild", "Black")
        self.assertTrue(c.color == "Black")
        c.set_color_of_wild("Red")
        self.assertTrue(c.color == "Red")

    def test_invalid_color_of_wild(self):
        c = UnoCard(-1, "Wild", "Black")
        self.assertRaises(ValueError, UnoCard.set_color_of_wild, c, "Stupendous")

    def test_invalid_card_color_set(self):
        c = UnoCard(0, "Number", "Red")
        self.assertRaises(ValueError, UnoCard.set_color_of_wild, c, "Blue")

if __name__ == '__main__':
    unittest.main()

