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
        self.table.trick = Trick()
        self.table.trick.cards = [Card(1, "Hearts"), Card(1, "Spades"), Card(4, "Diamonds"), Card(6, "Clubs")]

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
        self.assertTrue(self.table.is_valid_guess("1+1+1+1"))
        self.assertTrue(self.table.is_valid_guess("(1+1+1)+1"))
        self.assertTrue(self.table.is_valid_guess("1+1+(1+(1))"))
        self.assertTrue(self.table.is_valid_guess("((1+1))"))

        self.assertFalse(self.table.is_valid_guess("1+"))
        self.assertFalse(self.table.is_valid_guess("(1+1"))
        self.assertFalse(self.table.is_valid_guess("(1+)1"))
        self.assertFalse(self.table.is_valid_guess("+"))

    def test_guess_legality(self):
        self.assertTrue(self.table.is_legal_guess("1+1-4+6"))
        self.assertTrue(self.table.is_legal_guess("(6*4*1)+1"))
        self.assertTrue(self.table.is_legal_guess("1+1/(4+(6))"))

        self.assertFalse(self.table.is_legal_guess("1+1%4+6"))
        self.assertFalse(self.table.is_legal_guess("(6*4*6)+1"))
        self.assertFalse(self.table.is_legal_guess("1/(4+(6))"))

    def test_guess_correctness(self):
        self.assertTrue(self.table.is_correct_guess("6 + 6 + 6 + 6"))
        self.assertFalse(self.table.is_correct_guess("1 + 1 + 1 + 1"))

    def test_solvability(self):
        self.assertTrue(self.table.find_solution() != False)

    def test_solve(self):
        self.table.trick = Trick()
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

if __name__ == '__main__':
    unittest.main()
