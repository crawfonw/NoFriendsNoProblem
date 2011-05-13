import unittest
from UnoCardObjects import UnoCard
from UnoDeckObjects import UnoDeck

class TestUnoDeck(unittest.TestCase):

    def setUp(self):
        self.deck = UnoDeck()

    def test_deck_size(self):
        self.assertEqual(len(self.deck.cards), 108)

    def test_cards_in_deck(self):
        s = str(self.deck.cards)
        colors = ['Blue', 'Green', 'Red', 'Yellow']
        for value in range(0, 10):
            for color in colors:
                self.assertTrue(str(UnoCard(value, 'Number', color)) in s)

        types = ['Draw Two', 'Reverse', 'Skip']
        for color in colors:
            for t in types:
                    self.assertTrue(str(UnoCard(-1, t, color)) in s)

        self.assertTrue(str(UnoCard(-1, 'Wild', 'Black')) in s)

if __name__ == '__main__':
    unittest.main()
