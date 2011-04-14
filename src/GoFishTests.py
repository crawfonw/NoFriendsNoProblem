import unittest
from GoFishTableObjects import GoFishTable
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card

class GoFishTests(unittest.TestCase):
    def setUp(self):
        self.table = GoFishTable(2) # assume two players

    def test_initial_state(self):
        self.assertEqual(len(self.table.deck.cards), 38) # 38 cards left in deck after dealing
        self.assertEqual(len(self.table.players[0].hand), 7) # each player has seven cards
        self.assertEqual(len(self.table.players[1].hand), 7)

