import unittest
from ERSPlayerObjects import ERSPlayer
from CardObjects import Card

class TestERSPlayer(unittest.TestCase):

    def setUp(self):
        self.player = SlapJackPlayer

    def test_initial_state(self):
        self.assertTrue(len(self.player.pile.cards, 0))

    def test_flip(self):
        self.player.pile.cards = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        ret = self.player.flip()
        self.assertTrue(len(self.player.pile.cards), 2)
        self.assertTrue(ret.same_as(Card(13, "Hearts")))

    def test_slap_correct(self):
        self.assertTrue(self.player.slap(Card(11, "Hearts")))

    def test_slap_incorrect(self):
        self.assertFalse(self.player.slap(Card(7, "Diamonds")))
