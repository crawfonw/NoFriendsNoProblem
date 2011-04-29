import random
from CardObjects import Card
from DeckObjects import Deck

class TwentyFourDeck(Deck):

    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for value in range(1, 11):
            for suit in suits:
                self.cards.append(Card(value, suit))
