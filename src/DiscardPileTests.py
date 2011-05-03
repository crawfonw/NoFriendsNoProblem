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

    def test_has_double(self):
        self.pile.add(Card(1, "Clubs"))
        self.pile.add(Card(1, "Diamonds"))
        self.assertTrue(self.pile.has_double())

    def test_hasnt_double(self):
        self.pile.add(Card(1, "Clubs"))
        self.pile.add(Card(2, "Diamonds"))
        self.assertFalse(self.pile.has_double())

    def test_hasnt_double_empty(self):
        self.assertFalse(self.pile.has_double())

    def test_hasnt_double_too_few_cards(self):
        self.pile.add(Card(6, "Spades"))
        self.assertFalse(self.pile.has_double())

    def test_has_sandwich(self):
        self.pile.add(Card(1, "Clubs"))
        self.pile.add(Card(2, "Hearts"))
        self.pile.add(Card(1, "Diamonds"))
        self.assertTrue(self.pile.has_sandwich())

    def test_hasnt_sandwich(self):
        self.pile.add(Card(2, "Clubs"))
        self.pile.add(Card(1, "Hearts"))
        self.pile.add(Card(1, "Diamonds"))
        self.assertFalse(self.pile.has_sandwich())

    def test_hasnt_sandwich_empty(self):
        self.assertFalse(self.pile.has_sandwich())

    def test_hasnt_sandwich_too_few_cards(self):
        self.pile.add(Card(1, "Clubs"))
        self.assertFalse(self.pile.has_sandwich())
        self.pile.add(Card(1, "Hearts"))
        self.assertFalse(self.pile.has_sandwich())

if __name__ == '__main__':
    unittest.main()

