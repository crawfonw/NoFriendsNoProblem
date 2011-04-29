import unittest
from TwentyFourTableObjects import TwentyFourTable
from TwentyFourPlayerObjects import TwentyFourPlayer
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card
from TrickObjects import Trick

class TwentyFourTests(unittest.TestCase):
    def setUp(self):
        self.table = TwentyFourTable()
        self.correct_valid_guess = [Card(6, "Spades"), Operator("+"), Card(6, "Clubs"), Operator("+"), Card(6, "Diamonds"), Operator("+"), Card(6, "Hearts")]
        self.incorrect_valid_guess = [Card(1, "Spades"), Operator("+"), Card(1, "Clubs"), Operator("+"), Card(1, "Diamonds"), Operator("+"), Card(1, "Hearts")]
        self.incorrect_invalid_guess = [Card(1, "Spades"), Operator("+")]

    def test_initial_state(self):
        self.assertEqual(len(self.table.players), 2) # game has exactly two players
        self.assertEqual(len(self.table.players[0].hand), 20) # each player starts with exactly twenty cards
        self.assertEqual(len(self.table.players[1].hand), 20)
        self.assertEqual(len(self.table.players[0].points), 0) # each player starts with exactly zero points
        self.assertEqual(len(self.table.players[1].points), 0)

    def test_buzz_in(self):
        self.table.players[0].buzz_in()
        self.assertTrue(self.table.buzzed_in == self.table.players[0])

    def test_guess_validity(self):
        self.assertTrue(self.table.is_valid_guess(self.incorrect_valid_guess))
        self.assertFalse(self.table.is_valid_guess(self.incorrect_invalid_guess))

    def test_guess_correctness(self):
        self.assertTrue(self.table.is_correct_guess(self.correct_valid_guess))
        self.assertFalse(self.table.is_correct_guess(self.incorrect_valid_guess))

    def test_solvability(self):
        self.table.trick.cards = [Card(1, "Hearts"), Card(1, "Spades"), Card(4, "Diamonds"), Card(6, "Clubs")]
        self.assertTrue(self.table.is_solvable(self.trick))

    def test_solve(self):
        self.trick.cards = [Card(1, "Hearts"), Card(1, "Spades"), Card(4, "Diamonds"), Card(6, "Clubs")]
        self.table.solve(players[0])
        self.assertEqual(len(self.table.players[0].hand), 22) # player who successfully solves trick takes the cards
        self.assertEqual(len(self.table.players[1].hand), 18)

    def test_elimination_winning_condition(self):
        self.table.players[0].hand.append(self.table.players[1].hand) # player 0 absorbs player 1's hand
        self.table.players[1].hand = []
        self.assertEqual(self.table.winner(), self.table.players[0]) # assert that player 0 has won

    def test_point_winning_condition(self):
        self.table.players[0].points = 15 # player 0 accumulates 15 points
        self.assertEqual(self.table.winner(), self.table.players[0]) # assert that player 0 has won
