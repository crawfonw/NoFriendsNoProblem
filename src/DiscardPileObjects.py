
from DeckObjects import Deck

class DiscardPile(Deck):
    
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]

    def has_double(self):
        if len(self.cards) > 1:
            return not (self.cards[-1] < self.cards[-2]) and \
                   not (self.cards[-2] < self.cards[-1])
        else:
            return False

    def has_sandwich(self):
        if len(self.cards) > 2:
            return not (self.cards[-1] < self.cards[-3]) and \
                   not (self.cards[-3] < self.cards[-1])
        else:
            return False
