from TableObjects import Table
from ERSPlayerObjects import ERSPlayer
from DiscardPileObjects import DiscardPile
from DeckObjects import Deck
from time import sleep

class ERSTable(Table):
   
    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.pile = DiscardPile()
        self.deck.shuffle()
        for i in range(player_count):
            self.players.append(ERSPlayer())
        self.deal_all()

    def get_winner(self):
        for i in range(len(self.players)):
            return i

    def play_game(self):
        player = 0
        while not self.winner():
            value = 0
            if len(self.pile.cards) > 0:
                value = self.pile.peek().value
            if value == 1 or value > 10:
                player = self.war(player)
            else:
                if player == 0:
                    raw_input(_("Play a card!"))
                card = self.players[player].flip()
                print(_("Player {} plays the {}!").format(player, card))
                self.pile.add(card)
            self.wait_for_slap(0.25)
            player = ((player + 1) % len(self.players))
        print(_("Player {} wins!").format(self.get_winner()))

    def wait_for_slap(self, t):
        sleep(t)

    def war(self, player):
        value = self.pile.peek().value
        num = 0
        if value == 1:
            num = 4
        else:
            num = value - 10
        for i in range(num):
            card = self.players[player].flip()
            print(_("Player {} plays the {}!").format(player, card))
            self.pile.add(card)
            value = card.value
            self.wait_for_slap(0.25)
            if value == 1 or value > 10:
                return player
        self.players[player].cards = self.pile.cards + self.players[player].hand
        self.pile.cards = []
        return player - 1        

    def winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                return True
        return False
