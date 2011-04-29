import unittest
from GoFishHumanPlayerObjects import GoFishHumanPlayer
from GoFishAIPlayerObjects import GoFishAIPlayer
from CardObjects import Card

class TestGoFishHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.player = GoFishHumanPlayer()
        self.other = GoFishAIPlayer()

    def test_take_card(self):
        self.other.hand = [Card(1, "Spades")]
        self.assertEqual(len(self.player.hand), 0)
        self.assertEqual(len(self.other.hand), 1)
        self.player.take_card(self.other, 0)
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(len(self.other.hand), 0)

if __name__ == "__main__":
    unittest.main()
