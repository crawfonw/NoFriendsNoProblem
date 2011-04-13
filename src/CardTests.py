import unittest
from CardObjects import Card

class TestCard(unittest.TestCase):
    '''
    Testing for invalid values is not needed
    due to the flexibility of defining cards
    for various games.
    '''

    def setUp(self):
        pass

    def test_to_string(self):
        c = Card(13, "Hearts")
        self.assertEqual(str(c), "King of Hearts")

    def test_init_suit_with_empty_string(self):
        self.assertRaises(ValueError, Card, 13, "")

    def test_get_name(self):
        c = Card(2, "Clubs")
        self.assertEqual(c.get_name(), "2")

    def test_get_name_with_joker(self):
        c = Card(0, "Jokers")
        self.assertEqual(c.get_name(), "Joker")

    def test_invalid_number(self):
        self.assertRaises(ValueError, Card, 14, "Hearts")

    def test_get_face_name(self):
        c = Card(12, "Diamonds")
        self.assertEqual(c.get_name(), "Queen")

if __name__ == '__main__':
    unittest.main()

