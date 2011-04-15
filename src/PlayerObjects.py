from DeckObjects import Deck

class Player(object):
    
    def __init__(self):
        self.hand = []
        
    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
        except:
            pass

    def has_card_index(self, value):
        for i in range(len(self.hand)):
            if self.hand[i].value == value:
                return i
        return -1

    def play_card(self):
        return self.hand.pop()
