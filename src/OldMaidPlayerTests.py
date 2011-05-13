import unittest
from OldMaidPlayerObjects import OldMaidPlayer
from CardObjects import Card

class TestOldMaidPlayer(unittest.TestCase):

    def setUp(self):
        self.player = OldMaidPlayer()
        self.other = OldMaidPlayer()

    def test_initial_state(self):
        self.assertEqual(len(self.player.hand), 0) # starts with no cards

    def test_has_old_maid(self):
        self.player.hand = [Card(0, "Joker")]
        self.assertTrue(self.player.has_old_maid())
        self.assertFalse(self.other.has_old_maid())

    def test_earned_no_discard(self):
        self.player.hand = [Card(13, "Diamonds"), Card(12, "Clubs"), Card(11, "Hearts")]
        self.assertEqual(self.player.check_discard(), -1)

    def test_earned_discard(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs")]
        self.assertEqual(self.player.check_discard(), 13)

    def test_remove_card(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts"), Card(13, "Spades")]
        self.assertEqual(len(self.player.hand), 4)
        self.player.remove_card(Card(13,"Clubs"))
        self.assertEqual(len(self.player.hand), 3)

    def test_remove_two(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts"), Card(13, "Spades")]
        self.assertEqual(len(self.player.hand), 4)
        self.player.remove_two(13)
        self.assertEqual(len(self.player.hand), 2)

    def test_update_score(self):
        self.player.hand = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts"), Card(13, "Spades")]
        self.assertEqual(len(self.player.hand), 4)
        self.player.update_score()
        self.assertEqual(len(self.player.hand), 0)

if __name__ == '__main__':
    unittest.main()
