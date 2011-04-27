import unittest
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card
from TableObjects import Table

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table(2)
    
    def test_deal(self):
        self.table.deck.cards = [Card(13, "Hearts"), Card(13, "Spades"), Card(13, "Diamonds"), Card(13, "Clubs")]
        self.table.deal(2)

        for i in range(2):
            self.assertTrue(self.table.players[0].hand[i].same_as([Card(13, "Spades"), Card(13, "Clubs")][i]))

        for i in range(2):
            self.assertTrue(self.table.players[1].hand[i].same_as([Card(13, "Hearts"), Card(13, "Diamonds")][i]))
    
    def test_deal_without_enough_cards(self):
        self.table.deck.cards = [Card(13, "Hearts"), Card(13, "Spades"), Card(13, "Diamonds"), Card(13, "Clubs")]
        self.assertRaises(IndexError, self.table.deal, 3)

    def test_simple_game(self):
        self.table.deck.cards = [Card(2, "Hearts"), Card(13, "Spades"), Card(13, "Diamonds"), Card(13, "Clubs")]
        self.assertEqual(self.table.play_game(), self.table.players[0])

if __name__ == '__main__':
    unittest.main()

