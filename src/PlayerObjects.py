from DeckObjects import Deck

class Player(object):
    
    def __init__(self):
        self.hand = []
        
    def draw_from(self, deck):
        self.hand.insert(0, deck.draw())

    def play_card(self):
        return self.hand.pop()
