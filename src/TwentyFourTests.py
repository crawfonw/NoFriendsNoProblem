import unittest
from TwentyFourTableObjects import TwentyFourTable
from TwentyFourPlayerObjects import TwentyFourPlayer
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card
from TrickObjects import Trick

class TestTwentyFour(unittest.TestCase):
    def setUp(self):
        self.table = TwentyFourTable()
        self.correct_valid_guess = "6 + 6 + 6 + 6"
        self.incorrect_valid_guess = "1 + 1 + 1 + 1"
        self.incorrect_invalid_guess = "1 +"
        self.trick = Trick()
        self.trick.cards = [Card(1, "Hearts"), Card(1, "Spades"), Card(4, "Diamonds"), Card(6, "Clubs")]

    def test_initial_state(self):
        self.assertEqual(len(self.table.players), 2) # game has exactly two players
        self.assertEqual(len(self.table.players[0].hand), 20) # each player starts with exactly twenty cards
        self.assertEqual(len(self.table.players[1].hand), 20)
        self.assertEqual(self.table.players[0].points, 0) # each player starts with exactly zero points
        self.assertEqual(self.table.players[1].points, 0)

    def test_play_round(self):
        self.table.play_round()
        self.assertEqual(len(self.table.players[0].hand), 18)
        self.assertEqual(len(self.table.players[1].hand), 18)

    def test_buzz_in(self):
        self.table.buzz_in(0)
        self.assertTrue(self.table.buzzed_in == 0)

    def test_guess_validity(self):
        self.assertTrue(self.table.is_valid_guess(self.incorrect_valid_guess))
        self.assertFalse(self.table.is_valid_guess(self.incorrect_invalid_guess))

    def test_guess_correctness(self):
        self.assertTrue(self.table.is_correct_guess(self.correct_valid_guess))
        self.assertFalse(self.table.is_correct_guess(self.incorrect_valid_guess))

    def test_solvability(self):
        self.assertTrue(self.table.is_solvable(self.trick))

    def test_solve(self):
        self.table.play_round()
        self.table.solve(0)
        self.assertEqual(len(self.table.players[0].hand), 22) # player who successfully solves trick takes the cards
        self.assertEqual(len(self.table.players[1].hand), 18)
        self.assertEqual(self.table.players[0].points, 1)

    def test_elimination_winning_condition(self):
        self.table.players[0].hand.extend(self.table.players[1].hand) # player 0 absorbs player 1's hand
        self.table.players[1].hand = []
        self.assertEqual(self.table.winner(), 0) # assert that player 0 has won

    def test_point_winning_condition(self):
        self.table.players[0].points = 15 # player 0 accumulates 15 points
        self.assertEqual(self.table.winner(), 0) # assert that player 0 has won
