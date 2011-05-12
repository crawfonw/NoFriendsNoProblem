import unittest
from UnoDeckObjects import UnoDeck

class TestUnoDeck(unittest.TestCase):

    def setUp(self):
        self.deck = UnoDeck()

    def test_size(self):
        self.assertEqual(len(self.deck.cards), 108)

if __name__ == '__main__':
    unittest.main()
