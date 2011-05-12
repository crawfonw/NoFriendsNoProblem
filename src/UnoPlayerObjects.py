from PlayerObjects import Player

class UnoPlayer(Player): 

    def hand_is_empty(self):
        return len(self.hand) == 0

    def is_valid_move(self, card, top):
        return card.type == 'Wild' or \
                top.type == 'Wild' or \
                card.value == top.value or \
                card.color == top.color or \
                (card.type == 'Skip' and top.type == 'Skip') or \
                (card.type == 'Reverse' and top.type == 'Reverse') or \
                (card.type == 'Draw Two' and top.type == 'Draw Two')

    def play_card(self, card, pile):
        pass

    def print_hand(self):
        s = ''
        for card in self.hand:
            s += str(card)
        print 'Your hand contains:\n%s\n' % s
