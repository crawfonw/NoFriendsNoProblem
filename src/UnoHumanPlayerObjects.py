from UnoPlayerObjects import UnoPlayer

class HumanUnoPlayer(UnoPlayer):

    def player_type(self):
        return 0

    def card_index_in_hand(self, card):
        for i, c in enumerate(self.hand):
            if str(card) == str(c):
                return i
        return -1

    def play_card(self, card, pile):
        index = self.card_index_in_hand(card)
        if index == -1:
            print 'That card is not in your hand!'
        elif self.is_valid_move(card, pile.peek()):
            pile.add(card)
            self.hand = self.hand[:index] + self.hand[index + 1:]
        else:
            print 'That is not a valid move!'
