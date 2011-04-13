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
        for card1, card2 in map(None, self.table.players[0].hand, [Card(13, "Spades"), Card(13, "Clubs")]):
            self.assertTrue(card1.same_as(card2))

        for card1, card2 in map(None, self.table.players[1].hand, [Card(13, "Hearts"), Card(13, "Diamonds")]):
            self.assertTrue(card1.same_as(card2))
    
    def test_deal_without_enough_cards(self):
        self.table.deck.cards = [Card(13, "Hearts"), Card(13, "Spades"), Card(13, "Diamonds"), Card(13, "Clubs")]
        self.assertRaises(IndexError, self.table.deal, 3)

    def test_simple_game(self):
        self.table.deck.cards = [Card(2, "Hearts"), Card(13, "Spades"), Card(13, "Diamonds"), Card(13, "Clubs")]
        self.assertEqual(self.table.play_game(), self.table.players[0])

if __name__ == '__main__':
    unittest.main()

