import unittest

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.deck = Deck()
        self.player.hand = ["Ace of Hearts", "Ace of Spades", "Ace of Diamonds", "Ace of Clubs"]
        self.deck.cards =  ["King of Hearts", "King of Spades", "King of Diamonds", "King of Clubs"]

    def test_draw(self):
        initial_hand_size = self.player.hand_size()
        self.assertEqual(initial_hand_size, 4)
        self.player.draw(self.deck.draw())
        self.assertEqual(self.player.hand_size(), initial_hand_size + 1)

    def test_play_card(self):
        initial_hand_size = self.player.hand_size()
        self.player.play_card("Ace of Spades")
        self.assertEqual(self.player.hand_size(), initial_hand_size - 1)

    def test_play_card_from_empty_hand(self):
        self.player.hand = []
        self.assertRaises(EmptyHandException, self.player.play_card())

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.cards =  ["King of Hearts", "King of Spades", "King of Diamonds", "King of Clubs"]

    def test_shuffle(self):
        sorted_deck = ["King of Hearts", "King of Spades", "King of Diamonds", "King of Clubs"].sort()
        self.deck.shuffle()
        self.deck.cards.sort()
        self.assertEqual(self.deck.cards, sorted_deck)
        self.assertEqual(len(self.deck.cards), 4)

    def test_draw(self):
        initial_length = len(self.deck.cards)
        self.assertEqual(self.deck.draw(), "King of Hearts")
        self.assertEqual(len(self.deck.cards), initial_length - 1)

    def test_draw_from_empty_deck(self):
        self.deck.cards = []
        self.assertRaises(EmptyDeckException, self.deck.draw())
        

if __name__ == '__main__':
    unittest.main()

