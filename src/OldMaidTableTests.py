import unittest
from OldMaidTableObjects import OldMaidTable
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card

class TestOldMaidTable(unittest.TestCase):
    
    def setUp(self):
        self.table = OldMaidTable(2) # assume two players

    def test_initial_state(self):
        self.assertEqual(len(self.table.deck.cards), 0)
        self.assertEqual(len(self.table.players[0].hand), 27)
        self.assertEqual(len(self.table.players[1].hand), 26)
       
    def test_get_loser_just_old_maid(self):
        self.table.players[0].hand = []
        self.table.players[1].hand = [Card(0, "Joker")]
        self.assertEqual(self.table.get_loser(),1)

    def test_get_winner_with_cards(self):
        self.table.players[0].hand = [Card(13, "Diamonds"), Card(8, "Hearts"), Card(0, "Joker")]
        self.table.players[1].hand = []
        self.assertEqual(self.table.get_loser(),0)

    def test_no_winner(self):
        self.table.players[0].hand = [Card(13, "Diamonds")]
        self.table.players[1].hand = [Card(0, "Joker")]
        self.assertEqual(self.table.winner(), False)

    def test_winner(self):
        self.table.players[0].hand = []
        self.table.players[1].hand = [Card(0, "Joker")]
        self.assertEqual(self.table.winner(), True)

if __name__ == '__main__':
    unittest.main()
