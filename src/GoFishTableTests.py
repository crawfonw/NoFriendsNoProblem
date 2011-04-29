import unittest
from GoFishTableObjects import GoFishTable
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card

<<<<<<< HEAD
class TestGoFish(unittest.TestCase):
=======
class TestGoFishTable(unittest.TestCase):
>>>>>>> 1d4f7e223504fcf507b5930c85bf019ac183089e
    def setUp(self):
        self.table = GoFishTable(2) # assume two players

    def test_initial_state(self):
        self.assertEqual(len(self.table.deck.cards), 38) # 38 cards left in deck after dealing
        self.assertEqual(len(self.table.players[0].hand), 7) # each player has seven cards
        self.assertEqual(len(self.table.players[1].hand), 7)

    def test_get_winner(self):
        self.table.players[1].score = 1
        self.assertEqual(self.table.get_winner(), 1)

    def test_get_winner_with_cards(self):
        self.table.players[0].hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        self.table.players[0].score = 2
        self.table.players[1].score = 1
        self.assertEqual(self.table.get_winner(), 0)

    def test_no_winner(self):
        self.table.players[0].hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        self.table.players[1].hand = [Card(13, "Spades")]
        self.assertEqual(self.table.winner(), False)

    def test_winner(self):
        self.table.players[1].hand = []
        self.assertEqual(self.table.winner(), True)

if __name__ == '__main__':
    unittest.main()
