from PlayerObjects import Player
from CardObjects import Card

class GoFishPlayer(Player):

    def __init__(self):
        self.hand = []
        self.score = 0

    def check_point(self):
        card_values = [0 for i in range(13)]
        for card in self.hand:
            card_values[card.value - 1] = card_values[card.value - 1] + 1
        try:
            return card_values.index(4) + 1
        except:
            return -1

    def remove_all(self, value):
        i = 0
        while i < len(self.hand):
            if self.hand[i].value == value:
                self.hand.remove(self.hand[i])
                i -= 1
            i += 1

    def update_score(self):
        four_of_a_kind = self.check_point()
        if four_of_a_kind > 0:
            self.remove_all(four_of_a_kind)
            print("You get a point!")
            self.score += 1

    def print_hand(self):
        print("Your hand contains:")
        for card in self.hand:
            print(card)

    def take_card(self, other, index):
        print("You take the {}!".format(other.hand[index]))
        self.hand = self.hand + [other.hand[index]]
        other.hand = other.hand[0:index] + other.hand[index+1:]

    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
            print("You got the {}".format(self.hand[0]))
        except:
            print("The deck is empty!")
            pass

    def play_round(self, others, deck):
        player = int(input("Choose a player: 0 - {} >>> ".format(len(others) - 1)))
        if not (0 <= player < len(others)):
            player = int(input("Choose a player: 0 - {} >>> ".format(len(others) - 1)))
        self.print_hand()
        value = int(input("Which card would you like to ask for? 1 - 13 >>> "))
        index = others[player].has_card_index(value)
        if index > -1:
            self.take_card(others[player], index)
        else:
            print("Go Fish!")
            self.draw_from(deck)
