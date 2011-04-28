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

    def test_peek(self):
        self.pile.add(Card(1, "Spades"))
        self.assertTrue(self.pile.peek().same_as(Card(1, "Spades")))

    def test_peek_multiple_cards(self):
        self.pile.add(Card(1, "Clubs"))
        self.pile.add(Card(1, "Diamonds"))
        self.pile.add(Card(1, "Hearts"))
        self.pile.add(Card(1, "Spades"))
        self.assertTrue(self.pile.peek().same_as(Card(1, "Spades")))

    def test_peek_no_cards(self):
        self.assertEqual(self.pile.peek(), None)

if __name__ == '__main__':
    unittest.main()

