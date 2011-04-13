
from DeckObjects import Deck

class DiscardPile(Deck):
    
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)
