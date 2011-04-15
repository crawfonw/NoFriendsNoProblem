from TableObjects import Table
from GoFishPlayerObjects import GoFishPlayer
from DeckObjects import Deck

class GoFishTable(Table):

    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        for i in range(player_count):
            self.players.append(GoFishPlayer())

    def get_winner(self):
        max_score_player = -1
        for i in range(len(self.players)):
            if player.score > max_score:
                max_score_player = i
        return max_score_player

    def play_game(self):
        self.deal(7)
        current_player = 0
        while not self.winner():
            print("Player {}:".format(current_player))
            self.players[current_player].play_round(self.players[0:current_player] + self.players[current_player+1:], self.deck)
            self.players[current_player].update_score()
            current_player = (current_player + 1) % (len(self.players))
        print("Player {} wins!".format(self.get_winner()))

    def winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                return True
        return False
