from CardObjects import Card
from PlayerObjects import Player
from DeckObjects import Deck
from DiscardPileObjects import DiscardPile

class Table(object):
    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        self.discard = DiscardPile()
        self.trick = []

        for i in range(player_count):
            self.players.append(Player())

    def deal(self, num_cards):
        if num_cards * len(self.players) > len(self.deck.cards):
            raise IndexError

        for i in range(num_cards):
            for player in self.players:
                player.draw_from(self.deck)

    def play_game(self):
        while not self.winner():
            self.trick = []
            self.deal(1)
            for player in self.players:
                self.trick.append(player.play_card())
        return self.winner()

    def winner(self):
        if len(self.trick) > 0:
            if self.trick[0] > self.trick[1]:
                return self.players[0]
            elif self.trick[0] < self.trick[1]:
                return self.players[1]
                

