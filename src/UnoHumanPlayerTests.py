import unittest

from DiscardPileObjects import DiscardPile

from UnoCardObjects import UnoCard
from UnoHumanPlayerObjects import HumanUnoPlayer

class TestUnoHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.player = HumanUnoPlayer()
        self.other = HumanUnoPlayer()
        self.discard = DiscardPile()

    def test_valid_color_move(self):
        self.player.hand = [UnoCard(0, 'Number', 'Red')]
        self.discard.cards = [UnoCard(7, 'Number', 'Red')]
        self.player.play_card(str(self.player.hand[0]), self.discard)
        self.assertTrue(self.player.hand_is_empty())
        self.assertEqual(str(self.discard.peek()), str(UnoCard(0, 'Number', 'Red')))

    def test_valid_number_move(self):
        self.player.hand = [UnoCard(0, 'Number', 'Red')]
        self.discard.cards = [UnoCard(0, 'Number', 'Yellow')]
        self.player.play_card(str(self.player.hand[0]), self.discard)
        self.assertTrue(self.player.hand_is_empty())
        self.assertEqual(str(self.discard.peek()), str(UnoCard(0, 'Number', 'Red')))

    def test_valid_wild_move(self):
        self.player.hand = [UnoCard(-1, 'Wild', 'Black')]
        self.discard.cards = [UnoCard(0, 'Number', 'Yellow')]
        self.player.play_card(str(self.player.hand[0]), self.discard)
        self.assertTrue(self.player.hand_is_empty())
        self.discard.cards
        self.assertEqual(str(self.discard.peek()), str(UnoCard(-1, 'Wild', 'Red')))

    def test_invalid_move(self):
        self.player.hand = [UnoCard(0, 'Number', 'Yellow')]
        self.discard.cards = [UnoCard(7, 'Number', 'Red')]
        self.player.play_card(str(self.player.hand[0]), self.discard)
        self.assertEqual(str(self.player.hand[0]), str(UnoCard(0, 'Number', 'Yellow')))
        self.assertEqual(str(self.discard.peek()), str(UnoCard(7, 'Number', 'Red')))

if __name__ == '__main__':
    unittest.main()
