from PlayerObjects import Player
from CardObjects import Card

class ERSPlayer(Player):
    
    def __init__(self):
        self.hand = []

    def flip(self):
        card = self.hand[-1]
        self.hand = self.hand[:-1]
        return card
