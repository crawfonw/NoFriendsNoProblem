import unittest
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.deck = Deck()
        self.player.hand = [Card(1, "Hearts"), Card(1, "Spades"), Card(1, "Diamonds"), Card(1, "Clubs")]
        self.deck.cards = [Card(13, "Hearts"), Card(13, "Spades"), Card(13, "Diamonds"), Card(13, "Clubs")]

    def test_draw_from(self):
        initial_hand_size = len(self.player.hand)
        self.assertEqual(initial_hand_size, 4)
        self.player.draw_from(self.deck)
        self.assertEqual(len(self.player.hand), initial_hand_size + 1)

    def test_play_card(self):
        initial_hand_size = len(self.player.hand)
        self.player.play_card()
        self.assertEqual(len(self.player.hand), initial_hand_size - 1)

    def test_play_card_from_empty_hand(self):
        self.player.hand = []
        self.assertRaises(IndexError, self.player.play_card)

if __name__ == '__main__':
    unittest.main()

