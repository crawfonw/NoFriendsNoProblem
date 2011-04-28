import unittest
from GoFishPlayerObjects import GoFishPlayer
from CardObjects import Card

class TestGoFishPlayer(unittest.TestCase):

    def setUp(self):
        self.player = GoFishPlayer()
        self.other = GoFishPlayer()

    def test_initial_state(self):
        self.assertEqual(len(self.player.hand), 0) # starts with no cards
        self.assertEqual(self.player.score, 0) # starts with no points

    def test_earned_no_point(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        self.assertEqual(self.player.check_point(), -1)

    def test_earned_point(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts"), Card(13, "Spades")]
        self.assertEqual(self.player.check_point(), 13)

    def test_remove_all(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts"), Card(13, "Spades")]
        self.assertEqual(len(self.player.hand), 4)
        self.player.remove_all(13)
        self.assertEqual(len(self.player.hand), 0)

    def test_update_score(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts"), Card(13, "Spades")]
        self.assertEqual(self.player.score, 0)
        self.assertEqual(len(self.player.hand), 4)
        self.player.update_score()
        self.assertEqual(self.player.score, 1)
        self.assertEqual(len(self.player.hand), 0)

    def test_take_card(self):
        self.other.hand = [Card(1, "Spades")]
        self.assertEqual(len(self.player.hand), 0)
        self.assertEqual(len(self.other.hand), 1)
        self.player.take_card(self.other, 0)
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(len(self.other.hand), 0)

if __name__ == '__main__':
    unittest.main()
