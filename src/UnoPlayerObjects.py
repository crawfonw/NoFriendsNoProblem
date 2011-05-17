from PlayerObjects import Player

import gettext
_ = gettext.gettext

class UnoPlayer(Player): 

    def hand_is_empty(self):
        return len(self.hand) == 0

    def is_valid_move(self, card, top):
        return card.type == _('Wild') or \
                top.type == _('Wild') or \
                card.value == top.value or \
                card.color == top.color or \
                (card.type == _('Skip') and top.type == _('Skip')) or \
                (card.type == _('Reverse') and top.type == _('Reverse')) or \
                (card.type == _('Draw Two') and top.type == _('Draw Two'))

    def play_card(self, card, pile):
        pass

    def print_hand(self):
        s = ''
        for card in self.hand:
            s += str(card)
        print _('Your hand contains:\n{}\n').format(s)
