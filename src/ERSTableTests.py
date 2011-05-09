import unittest
from ERSTableObjects import ERSTable
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card

class TestERSTable(unittest.TestCase):

    def setUp(self):
        self.table = ERSTable(2)

    def test_initial_state(self):
        self.assertEqual(len(self.table.pile.cards), 0)
        self.assertEqual(len(self.table.players[0].hand), 26)
        self.assertEqual(len(self.table.players[1].hand), 26)

    def test_get_winner(self):
        self.table.players[0].hand.extend(self.table.players[1].hand)
        self.table.players[1].hand = []
        self.assertEqual(self.table.get_winner(), 0)

    def test_winner_exists1(self):
        self.table.players[0].hand.extend(self.table.players[1].hand)
        self.table.players[1].hand = []
        self.assertTrue(self.table.winner())

    def test_winner_exists2(self):
        self.table.players[1].hand.extend(self.table.players[0].hand)
        self.table.players[0].hand = []
        self.assertTrue(self.table.winner())

    def test_no_winner_exists1(self):
        self.assertFalse(self.table.winner())

    def test_no_winner_exists2(self):
        self.table.players[0].hand.extend(self.table.players[1].hand)
        self.table.players[1].hand = self.table.players[0].hand[0]
        self.table.players[0].hand = self.table.players[0].hand[1:]
        self.assertFalse(self.table.winner())

if __name__ == '__main__':
    unittest.main()




