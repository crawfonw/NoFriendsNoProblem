from TableObjects import Table
from SlapJackPlayerObjects import SlapJackPlayer
from DiscardPileObjects import DiscardPile

class SlapJackTable(Table):
   
    def __init__(self, player_count=2):
        self.players = []
        self.pile = DiscardPile()

    def get_winner(self):
        pass

    def play_game(self):
        pass

    def winner(self):
        pass
