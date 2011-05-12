import random
from UnoCardObjects import UnoCard
from DeckObjects import Deck

class UnoDeck(Deck):

    def __init__(self):
        self.cards = []
        colors = ['Blue', 'Green', 'Red', 'Yellow']
        for value in range(0, 10):
            for color in colors:
                self.cards.append(UnoCard(value, 'Number', color))
                self.cards.append(UnoCard(value, 'Number', color))

        types = ['Draw Two', 'Reverse', 'Skip']
        for color in colors:
            for t in types:
                for value in range(2):
                    self.cards.append(UnoCard(-1, t, color))

        for i in range(4):
            self.cards.append(UnoCard(-1, 'Wild', 'Black'))
