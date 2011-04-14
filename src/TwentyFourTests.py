import unittest
from TwentyFourTableObjects import TwentyFourTable
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card
from TrickObjects import Trick

class TwentyFourTests(unittest.TestCase):
    def setUp(self):
        self.table = TwentyFourTable()

    def test_initial_state(self):
        self.assertEqual(len(self.table.players), 2) # game has exactly two players
        self.assertEqual(len(self.table.players[0].hand), 20) # each player starts with exactly twenty cards
        self.assertEqual(len(self.table.players[1].hand), 20)

    def test_solvability(self):
        self.table.trick.cards = [Card(1, "Hearts"), Card(1, "Spades"), Card(4, "Diamonds"), Card(6, "Clubs")]
        self.assertTrue(self.table.is_solvable(self.trick))

    def test_solve(self):
        self.trick.cards = [Card(1, "Hearts"), Card(1, "Spades"), Card(4, "Diamonds"), Card(6, "Clubs")]
        self.table.solve.(players[0])
        self.assertEqual(len(self.table.players[0].hand), 22) # player who successfully solves trick takes the cards
        self.assertEqual(len(self.table.players[1].hand), 18)

    def test_winning_condition(self):
        self.table.players[0].hand.append(self.table.players[1].hand) # player 0 absorbs player 1's hand
        self.table.players[1].hand = []
        self.assertEqual(self.table.play_game(), self.table.players[0]) # assert that player 0 has won

