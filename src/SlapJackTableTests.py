import unittest
from GoFishTableObjects import GoFishTable
from PlayerObjects import Player
from DeckObjects import Deck
from CardObjects import Card

class TestSlapJackTable(unittest.TestCase):

    def setUp(self):
        self.table = TestSlapJackTable(2)

    def test_initial_state(self):
        self.assertEqual(len(self.table.pile), 0)
        self.assertEqual(len(self.table.players[0].pile.cards), 26)
        self.assertEqual(len(self.table.players[1].pile.cards), 26)

    def test_get_winner(self):
        self.table.players[0].pile.cards.extend(self.table.players[1].pile.cards)
        self.table.players[1].pile.cards = []
        self.assertEqual(self.table.get_winner(), 0)

    def test_winner_exists1(self):
        self.table.players[0].pile.cards.extend(self.table.players[1].pile.cards)
        self.table.players[1].pile.cards = []
        self.assertTrue(self.table.winner())

    def test_winner_exists2(self):
        self.table.players[1].pile.cards.extend(self.table.players[0].pile.cards)
        self.table.players[0].pile.cards = []
        self.assertTrue(self.table.winner())

    def test_no_winner_exists1(self):
        self.assertFalse(self.table.winner())

    def test_no_winner_exists2(self):
        self.table.players[0].pile.cards.extend(self.table.players[1].pile.cards)
        self.table.players[1].pile.cards = self.table.players[0].pile.cards[0]
        self.table.players[0].pile.cards = self.table.players[0].pile.cards[1:]
        self.assertFalse(self.table.winner())

    def test_no_cards_added_to_player_pile_on_incorrect_slap(self):
        self.table.players[0].pile.cards = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        self.table.players[1].pile.cards = [[Card(1, "Diamonds"), Card(1, "Clubs"), Card(1, "Hearts")]]
        self.table.pile.add(self.table.players[0].flip())
        self.table.players[1].slap(self.table.pile.peek())
        self.assertEqual(len(self.table.players[0].pile.cards), 2)
        self.assertEqual(len(self.table.players[1].pile.cards), 3)
        self.assertEqual(len(self.table.pile), 1)
        self.assertTrue(self.table.pile.peek().same_as(Card(13, "Hearts")))
        
    def test_cards_added_to_player_pile_on_incorrect_slap(self):
        self.table.players[0].pile.cards = [Card(13, "Diamonds"), Card(13, "Clubs"), Card(13, "Hearts")]
        self.table.players[1].pile.cards = [[Card(11, "Spades")]
        self.table.pile.cards = [Card(2, "Clubs"), Card(2, "Hearts")]
        self.table.pile.add(self.table.players[1].flip())
        self.table.players[1].slap(self.table.pile.peek())
        self.assertEqual(len(self.table.players[0].pile.cards), 3)
        self.assertEqual(len(self.table.players[1].pile.cards), 3)
        self.assertEqual(len(self.table.pile), 0)
        self.assertTrue(self.table.pile[0].same_as(Card(2, "Clubs")))
        self.assertTrue(self.table.pile[1].same_as(Card(2, "Hearts")))
        self.assertTrue(self.table.pile[2].same_as(Card(11, "Spades")))

if __name__ == '__main__':
    unittest.main()





