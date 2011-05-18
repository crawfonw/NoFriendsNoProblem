import random
from CardObjects import Card

class Deck(object):

    def __init__(self, jokers=False):
        self.cards = []
        suits = [_("Clubs"), _("Diamonds"), _("Hearts"), _("Spades")]
        for value in range(1, 14):
            for suit in suits:
                self.cards.append(Card(value, suit))
        if jokers:
            self.cards.append(Card(0, _("Jokers")))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
