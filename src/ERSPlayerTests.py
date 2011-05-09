import unittest
from ERSPlayerObjects import ERSPlayer
from CardObjects import Card

class TestERSPlayer(unittest.TestCase):

    def setUp(self):
        self.player = ERSPlayer()

    def test_initial_state(self):
        self.assertEqual(len(self.player.hand), 0)

    def test_flip(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        ret = self.player.flip()
        self.assertTrue(len(self.player.hand), 2)
        self.assertTrue(ret.same_as(Card(13, "Hearts")))

if __name__ == '__main__':
    unittest.main()
