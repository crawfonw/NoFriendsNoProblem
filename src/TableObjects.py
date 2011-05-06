from CardObjects import Card
from PlayerObjects import Player
from DeckObjects import Deck
from DiscardPileObjects import DiscardPile
from TrickObjects import Trick

class Table(object):
    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        self.discard = DiscardPile()
        self.trick = Trick()
        self.trick.cards = []

        for i in range(player_count):
            self.players.append(Player())

    def deal(self, num_cards):
        if num_cards * len(self.players) > len(self.deck.cards):
            raise IndexError

        for i in range(num_cards):
            for player in self.players:
                player.draw_from(self.deck)

    def deal_all(self):
        player = 0
        while len(self.deck.cards) > 0:
            self.players[player].draw_from(self.deck)
            player = (player + 1) % len(self.players)

    def play_game(self):
        while not self.winner():
            self.trick.cards = []
            self.deal(1)
            for player in self.players:
                self.trick.cards.append(player.play_card())
        return self.winner()

    def winner(self):
        if len(self.trick.cards) > 0:
            if self.trick.cards[0] > self.trick.cards[1]:
                return self.players[0]
            elif self.trick.cards[0] < self.trick.cards[1]:
                return self.players[1]


