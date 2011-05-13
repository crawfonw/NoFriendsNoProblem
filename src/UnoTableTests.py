import unittest

from UnoTableObjects import UnoTable

class TestUnoTable(unittest.TestCase):

    def setUp(self):
        self.table = UnoTable(2)

    def test_initial_state(self):
        self.assertEqual(len(self.table.players[0].hand), 7)
        self.assertEqual(len(self.table.players[1].hand), 7)
        self.assertEqual(len(self.table.deck.cards), 94)

    def test_winner(self):
        self.assertFalse(self.table.winner())
        self.table.players[0].hand = []
        self.assertTrue(self.table.winner() != None)

    def test_get_winner(self):
        self.table.players[0].hand = []
        self.assertEqual(str(self.table.players[0]), str(self.table.get_winner()))

if __name__ == '__main__':
    unittest.main()
