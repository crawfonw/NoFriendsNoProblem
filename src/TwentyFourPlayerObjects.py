from PlayerObjects import Player
from CardObjects import Card

class TwentyFourPlayer(Player):

    def __init__(self):
        self.hand = []
        self.points = 0

