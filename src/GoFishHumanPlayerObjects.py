from GoFishPlayerObjects import GoFishPlayer

class GoFishHumanPlayer(GoFishPlayer):

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
        player = -1
        while not (0 <= player < len(others)):
            player = int(input("Choose a player: 0 - {} >>> ".format(len(others) - 1)))
        self.print_hand()
        value = int(input("Which card would you like to ask for? 1 - 13 >>> "))
        index = others[player].has_card_index(value)
        if index > -1:
            self.take_card(others[player], index)
        else:
            print("Go Fish!")
            self.draw_from(deck)
