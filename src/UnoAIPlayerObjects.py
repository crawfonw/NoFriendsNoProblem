import random

from UnoPlayerObjects import UnoPlayer

class AIUnoPlayer(UnoPlayer):

    def player_type(self):
        return 1

    def card_index_in_hand(self, card_str):
        for i, c in enumerate(self.hand):
            if card_str == str(c):
                return i
        return -1

    def play_card(self, card_str, pile):
        ret = False
        index = self.card_index_in_hand(card_str)
        if index == -1:
            print _('That card is not in your hand!')
        elif self.is_valid_move(self.hand[index], pile.peek()):
            pile.add(self.hand[index])
            self.hand = self.hand[:index] + self.hand[index + 1:]
            ret = True
        else:
            print _('That is not a valid move!')

        return ret

    def find_best_move(self, next_player, pile):
        colors = {_('Blue'):0, _('Green'):1, _('Red'):2, _('Yellow'):3}
        enum_colors, enum_values = self.enumerate_cards()
        top = colors[pile.peek().color]
        hand = str(self.hand)
        move = _('Draw')

        if len(enum_colors[top]) != 0: #play a card via color, highest priority
            move = str(random.choice(enum_colors[top]))

        if len(enum_values[pile.peek().value]) != 0 and move == _('Draw'):
            max_colors = 0
            for card in enum_values[pile.peek().value]:
                color_count = len(enum_colors[colors[card.color]])
                if color_count > max_colors:
                    max_colors = color_count
                    move = str(card)

        if _('Skip') in hand: #a skip?
            if len(next_player.hand) < 4 or move == 'Draw':
                if _('{} Skip').format(pile.peek().color) in hand:
                    move = _('{} Skip').format(pile.peek().color)
                elif pile.peek().type == _('Skip'):
                    move = self.find_correct_color_card_combination(colors.keys(), _('Skip'))
        if _('Draw Two') in hand: #a draw two?
            if len(next_player.hand) < 4 or move == _('Draw'):
                if _('{} Draw Two').format(pile.peek().color) in hand:
                    move = _('{} Draw Two').format(pile.peek().color)
                elif pile.peek().type == _('Draw Two'):
                    move = self.find_correct_color_card_combination(colors.keys(), _('Draw Two'))
        if _('Reverse') in hand: #a reverse?
            if len(next_player.hand) < 4 or move == _('Draw'):
                if _('{} Reverse').format(pile.peek().color) in hand:
                    move = _('{} Reverse').format(pile.peek().color)
                elif pile.peek().type == _('Reverse'):
                    move = self.find_correct_color_card_combination(colors.keys(), _('Reverse'))
        if _('Wild Card') in hand and move == _('Draw'): #if we have a wild, should we play it?
            index = self.card_index_in_hand(_('Wild Card'))
            self.hand[index].set_color_of_wild(self.find_max_colors())
            move = str(self.hand[index])
        return move

    def find_correct_color_card_combination(self, color_keys, card_type):
        for color in color_keys:
            s = '{} {}'.format(color, card_type)
            if self.card_index_in_hand(s) != -1:
                return s

    def enumerate_cards(self):
        colors = [[], [], [], []] #blue, green, red, yellow
        values = [[], [], [], [], [], [], [], [], [], [], []]
        for card in self.hand:
            if card.value > -1:
                values[card.value].append(card)
                if card.color == _('Blue'):
                    colors[0].append(card)
                elif card.color == _('Green'):
                    colors[1].append(card)
                elif card.color == _('Red'):
                    colors[2].append(card)
                elif card.color == _('Yellow'):
                    colors[3].append(card)
        return colors, values

    def find_max_colors(self):
        max_list = []
        colors = [[], [], [], []]
        for card in self.hand:
            if card.color == _('Blue'):
                colors[0].append(card)
            elif card.color == _('Green'):
                colors[1].append(card)
            elif card.color == _('Red'):
                colors[2].append(card)
            elif card.color == _('Yellow'):
                colors[3].append(card)
        for l in colors:
            if len(l) > len(max_list):
                max_list = l
        if len(max_list) == 0:
            return random.choice([_('Blue'), _('Green'), _('Red'), _('Yellow')])
        return max_list[0].color
