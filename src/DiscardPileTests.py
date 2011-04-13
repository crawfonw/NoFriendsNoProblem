import unittest
from DiscardPileObjects import DiscardPile
from CardObjects import Card

class TestDiscardPile(unittest.TestCase):

    def setUp(self):
        self.pile = DiscardPile()

    def test_add_to_discard_pile(self):
        size = len(self.pile.cards)
        c = Card(0, "Jokers")
        self.pile.add(c)
        self.assertEqual(len(self.pile.cards), size + 1)
        self.assertEqual(str(self.pile.cards[0]), "Joker")

if __name__ == '__main__':
    unittest.main()

