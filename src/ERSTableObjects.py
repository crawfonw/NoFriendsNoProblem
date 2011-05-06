from TableObjects import Table
from ERSPlayerObjects import ERSPlayer
from DiscardPileObjects import DiscardPile

class ERSTable(Table):
   
    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.pile = DiscardPile()
        self.deck.sheffle()
        for i in range(player_count):
            self.players.append(ERSPlayer())
        self.deal_all()

    def get_winner(self):
        pass

    def play_game(self):
        pass

    def winner(self):
        pass
