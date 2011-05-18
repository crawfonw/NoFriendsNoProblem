from TableObjects import Table
from GoFishHumanPlayerObjects import GoFishHumanPlayer
from GoFishAIPlayerObjects import GoFishAIPlayer
from DeckObjects import Deck

import gettext
_ = gettext.GNUTranslations(open("locales/sp/GoFishSpanish.mo", "rb")).ugettext

class GoFishTable(Table):

    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        self.players.append(GoFishHumanPlayer('Puny Human'))
        for i in range(player_count - 1):
            self.players.append(GoFishAIPlayer(_('Computer %s') % (i + 1)))
        self.deal(7)

        #interacting with GUI
        self.current_player = 0
        self.other_player = None

    def get_winner(self):
        max_score_player = -1
        for i in range(len(self.players)):
            if max_score_player == -1 or self.players[i].score > self.players[max_score_player].score:
                max_score_player = i
        return max_score_player
    
    def play_turn(self, card_value=None):
        ret = ''
        others = self.players[0:self.current_player] + self.players[self.current_player+1:]
        print _("Player %s:") % self.current_player
        if self.players[self.current_player].player_type() == 1: #is AI
            ret = self.players[self.current_player].play_round(others, self.deck)
        else: #is Human
            ret = self.players[self.current_player].play_round(card_value, self.players, self.other_player, self.deck)
        self.players[self.current_player].update_score()
        self.current_player = (self.current_player + 1) % (len(self.players))
        return ret

    def winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                return True
        return False
