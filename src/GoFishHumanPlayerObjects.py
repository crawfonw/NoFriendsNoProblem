from GoFishPlayerObjects import GoFishPlayer

class GoFishHumanPlayer(GoFishPlayer):

    def player_type(self):
        return 0

    def print_hand(self):
        print "Your hand contains: %s" % self.hand

    def take_card(self, other, index):
        ret = "You take the %s!" % other.hand[index]
        self.hand = self.hand + [other.hand[index]]
        other.hand = other.hand[0:index] + other.hand[index+1:]
        print ret
        return ret

    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
            ret = "You got the %s" % self.hand[0]
            return ret
        except:
            ret = "The deck is empty!"
            print ret
            return ret

    def play_round(self, card_value, others, player_id, deck):
        index = others[player_id].has_card_index(card_value)
        if index > -1:
            return self.take_card(others[player_id], index)
        else:
            ret = self.draw_from(deck)
            newret = "Go Fish! - %s" % ret
            print newret
            return newret
