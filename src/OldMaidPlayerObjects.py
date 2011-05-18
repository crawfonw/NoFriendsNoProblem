from PlayerObjects import Player
from CardObjects import Card

class OldMaidPlayer(Player):

    def __init__(self):
        self.hand = []

    def check_discard(self):
        card_values = [0 for i in range(13)]
        for card in self.hand:
            card_values[card.value - 1] = card_values[card.value - 1] + 1
        try:
            for i in range(13):
                if card_values[i] > 1:
                    return i+1
            return -1
        except:
            return -1

    def has_old_maid(self):
        for card in self.hand:
            if card.value == 0:
                return True
        return False

    def remove_card(self, card):
        for i in range(len(self.hand)):
            if self.hand[i].same_as(card):
                self.hand = self.hand[0:i] + self.hand[i+1:]
                return

    def remove_two(self, value):
        i = 0
        count = 0
        while i < len(self.hand) and count < 2:
            if self.hand[i].value == value:
                self.hand.remove(self.hand[i])
                i -= 1
                count += 1
            i += 1

    def update_score(self):
        two_of_a_kind = self.check_discard()
        while two_of_a_kind > 0:
            self.remove_two(two_of_a_kind)
            print _("Discard!")
            two_of_a_kind = self.check_discard()

    def print_hand(self):
        print _("Your hand contains:")
        for card in self.hand:
            print(card)
