from UnoPlayerObjects import UnoPlayer

class HumanUnoPlayer(UnoPlayer):

    def player_type(self):
        return 0

    def card_index_in_hand(self, card_str):
        for i, c in enumerate(self.hand):
            if card_str == str(c):
                return i
        return -1

    def play_card(self, card_str, pile):
        ret = False
        index = self.card_index_in_hand(card_str)
        if index == -1:
            pass
            #print 'That card is not in your hand!'
        elif self.is_valid_move(self.hand[index], pile.peek()):
            pile.add(self.hand[index])
            self.hand = self.hand[:index] + self.hand[index + 1:]
            ret = True
        else:
            pass
            #print 'That is not a valid move!'

        return ret
