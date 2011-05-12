import unittest

from UnoCardObjects import UnoCard
from UnoPlayerObjects import UnoPlayer

class TestUnoPlayer(unittest.TestCase):

    def setUp(self):
        self.player = UnoPlayer()

    def test_valid_color_move(self):
        self.assertTrue(self.player.is_valid_move(UnoCard(7, 'Number', 'Yellow'), UnoCard(0, 'Number', 'Yellow')))

    def test_valid_number_move(self):
        self.assertTrue(self.player.is_valid_move(UnoCard(0, 'Number', 'Yellow'), UnoCard(0, 'Number', 'Blue')))

    def test_valid_wild_move(self):
        self.assertTrue(self.player.is_valid_move(UnoCard(0, 'Number', 'Yellow'), UnoCard(-1, 'Wild', 'Black')))

    def test_invalid_move(self):
        self.assertFalse(self.player.is_valid_move(UnoCard(0, 'Number', 'Yellow'), UnoCard(8, 'Number', 'Red')))

if __name__ == '__main__':
    unittest.main()
