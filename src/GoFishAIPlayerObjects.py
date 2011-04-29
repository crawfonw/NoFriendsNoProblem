from GoFishPlayerObjects import GoFishPlayer
from random import randrange

class GoFishAIPlayer(GoFishPlayer):

    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
        except:
            pass

    def take_card(self, other, index):
        print("Opponent takes the {}!".format(other.hand[index]))
        self.hand = self.hand + [other.hand[index]]
        other.hand = other.hand[0:index] + other.hand[index+1:]

    def get_best_value(self):
        card_values = [0 for i in range(13)]
        for card in self.hand:
            card_values[card.value - 1] = card_values[card.value - 1] + 1
        try:
            return card_values.index(max(card_values)) + 1
        except:
            return -1

    def play_round(self, others, deck):
        player = randrange(len(others))
        value = self.get_best_value()
        index = others[player].has_card_index(value)
        if index > -1:
            self.take_card(others[player], index)
        else:
            print("Opponent fishes...")
            self.draw_from(deck)
