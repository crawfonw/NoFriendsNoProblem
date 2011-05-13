from TableObjects import Table
from OldMaidPlayerObjects import OldMaidPlayer
from DeckObjects import Deck
from CardObjects import Card
from random import randrange

class OldMaidTable(Table):

    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.deck.cards.append(Card(0, "Joker"))
        self.deck.shuffle()
        for i in range(player_count):
            self.players.append(OldMaidPlayer())
        self.deal_all()

    def get_loser(self):
        loser = -1
        for i in range(len(self.players)):
            if len(self.players[i].hand) != 0:
                loser = i
        return loser
    
    def play_game(self):
        for i in range(len(self.players)):
            self.players[i].update_score()
        player = 0
        while not self.winner():
            if player == 0: #human
                self.players[0].print_hand()
                input("Taking a card from the player on your left...")
                onleft = player - 1
                while len(self.players[onleft].hand) == 0:
                    onleft -= 1
                card_taken = self.players[onleft].hand[randrange(len(self.players[onleft].hand))]
                print("You take the {}".format(card_taken))
                self.players[0].hand.append(card_taken)
                self.players[onleft].remove_card(card_taken)
            else: #inhuman
                while len(self.players[onleft].hand) == 0:
                    onleft -= 1
                card_taken = self.players[onleft].hand[randrange(len(self.players[onleft].hand))]
                if (onleft%len(self.players)) != 0:
                    print("Player {} takes a card".format(player))
                else:
                    print("Player {} takes your {}".format(player, card_taken))
                self.players[player].hand.append(card_taken)
                self.players[onleft].remove_card(card_taken)
            self.players[player].update_score()
            player = ((player + 1) % len(self.players))
        print("Player {} loses!".format(self.get_loser()))

    def winner(self):
        count = 0
        for player in self.players:
            if len(player.hand) == 0:
                count += 1
        return count == (len(self.players) - 1)
