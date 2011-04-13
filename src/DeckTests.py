import unittest
from DeckObjects import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.joker_deck = Deck(True)

    def test_size(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_joker_size(self):
        self.assertEqual(len(self.joker_deck.cards), 53)

    def test_draw(self):
        initial_length = len(self.deck.cards)
        self.assertEqual(str(self.deck.draw()), "King of Spades")
        self.assertEqual(len(self.deck.cards), initial_length - 1)

    def test_draw_from_empty_deck(self):
        self.deck.cards = []
        self.assertRaises(IndexError, self.deck.draw)

if __name__ == '__main__':
    unittest.main()

