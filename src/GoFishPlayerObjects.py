from PlayerObjects import Player
from CardObjects import Card

class GoFishPlayer(Player):

    def __init__(self):
        self.hand = []
        self.score = 0

    def check_point(self):
        card_values = [0 for i in range(13)]
        for card in self.hand:
            card_values[card.value - 1] = card_values[card.value - 1] + 1
        try:
            return card_values.index(4) + 1
        except:
            return -1

    def remove_all(self, value):
        i = 0
        while i < len(self.hand):
            if self.hand[i].value == value:
                self.hand.remove(self.hand[i])
                i -= 1
            i += 1

    def update_score(self):
        four_of_a_kind = self.check_point()
        if four_of_a_kind > 0:
            self.remove_all(four_of_a_kind)
            print("You get a point!")
            self.score += 1

    def print_hand(self):
        print("Your hand contains:")
        for card in self.hand:
            print(card)

    def take_card(self, other, index):
        pass

    def draw_from(self, deck):
        pass

    def play_round(self, others, deck):
        pass
