from DiscardPileObjects import DiscardPile
from TableObjects import Table

from UnoDeckObjects import UnoDeck
from UnoHumanPlayerObjects import HumanUnoPlayer
from UnoAIPlayerObjects import AIUnoPlayer

class UnoTable(Table):

    def __init__(self, player_count = 2):
        self.players = []
        self.deck = UnoDeck()
        self.deck.shuffle()
        self.discard = DiscardPile()
        self.players.append(HumanUnoPlayer('Human 1'))
        for i in range(player_count - 1):
            self.players.append(AIUnoPlayer('Computer %s' % (i + 1)))

        self.deal(7)
        self.current_player = 0
        self.TURN_CONS = 1

    def get_winner(self):
        return self.winner()

    def play_game(self):
        self.shuffle_and_turn()
        while not self.winner():
            result = None
            if len(self.deck.cards) == 0:
                self.shuffle_and_turn()
            print "\n~~~~~%s's Turn~~~~~\n" % self.players[self.current_player]
            if self.players[self.current_player].player_type() == 1: #is AI
                move = self.players[self.current_player].find_best_move(self.players[(self.current_player + self.TURN_CONS) % (len(self.players))], self.discard)
                if move == 'Draw':
                    print '%s draws a card...' % (self.players[self.current_player])
                    self.players[self.current_player].draw_from(self.deck)
                    result = 'draw'
                else:
                    print '%s plays a %s' % (self.players[self.current_player], move)
                    result = self.players[self.current_player].play_card(move, self.discard)
            else: #is Human
                print '+==================================+\n| Cards in deck: %s' % len(self.deck.cards)
                print '| Top of the discard pile: %s\n|' % self.discard.peek()
                print '%s' % self.print_hand_count()
                print '+==================================+\n'
                print '***Your hand contains***\n%s\n' % self.players[self.current_player].hand
                move = raw_input('Please input your move, or draw:\n')
                if move.lower().strip() == 'draw': #draw a card
                    self.players[self.current_player].draw_from(self.deck)
                    print 'You draw a %s' % self.players[self.current_player].hand[0]
                    result = 'draw'
                else: #play a card
                    result = self.players[self.current_player].play_card(move, self.discard)
                    if not result:
                        print 'That is not a valid card/move!\n'
                    else:
                        print '\n%s plays a %s' % (self.players[self.current_player], move)
            if result:
                if len(self.players[self.current_player].hand) == 1:
                    print '^^^^^ %s says UNO! ^^^^^' % self.players[self.current_player]
                self.determine_next_turn(move)
        print '%s wins!' % self.get_winner()

    def winner(self):
        for i, player in enumerate(self.players):
            if len(player.hand) == 0:
                return player

    def determine_next_turn(self, move):
        if 'Skip' in move:
            self.current_player = (self.current_player + 2 * self.TURN_CONS) % (len(self.players))
        elif 'Draw Two' in move:
            self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))
            self.players[self.current_player].draw_from(self.deck)
            self.players[self.current_player].draw_from(self.deck)
        elif 'Reverse' in move:
            self.TURN_CONS *= -1
            self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))
        elif 'Wild' in move and self.players[self.current_player].player_type() == 0:
            valid_color = False
            while not valid_color:
                color = raw_input('Please input the color for the wild card.\n')
                if color in ['Red', 'Blue', 'Green', 'Yellow']:
                    valid_color = True
                    self.discard.peek().set_color_of_wild(color)
                    self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))
        else:
            self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))

    def shuffle_and_turn(self):
        self.deck.cards.extend(self.discard.cards)
        self.discard.cards = []
        self.deck.shuffle()
        self.discard.add(self.deck.draw())

    def print_hand_count(self):
        s = ''
        for p in self.players:
            s += '| %s has %s cards in hand.\n' % (p, len(p.hand))
        return s.strip()




