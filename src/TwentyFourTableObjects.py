from TableObjects import Table
from TwentyFourPlayerObjects import TwentyFourPlayer
from TwentyFourDeckObjects import TwentyFourDeck
from TrickObjects import Trick

class TwentyFourTable(Table):
    def __init__(self):
        self.players = []
        for i in [0, 1]:
            self.players.append(TwentyFourPlayer())

        self.trick = Trick()

        self.deck = TwentyFourDeck()
        self.deck.shuffle()
        self.deal(20)

    def play_game(self):
        while not self.winner():
            if len(self.trick.cards) == 0:
                self.play_round()

            if not self.is_solvable(self.trick):
                continue

            for i in [0, 1]:
                print('Player {} has {} cards and {} points.'.format(i, len(self.players[i].hand), self.players[i].points))

            print('Make 24 out of these cards:')
            print('   {}'.format(self.trick.cards))

            print('Which player buzzes in?')
            try:
                self.buzz_in(int(raw_input('> ')))
            except Exception:
                print('Invalid input.')
                continue

            if self.buzzed_in != 0 and self.buzzed_in != 1:
                print('Invalid input.')
                continue

            print('What is player {}\'s guess?'.format(self.buzzed_in))
            guess = raw_input('> ')

            if not self.is_valid_guess(guess):
                print('Guess is invalid!')
                continue

            if not self.is_correct_guess(guess):
                print('That doesn\'t make 24!')
                continue

            print('Player {} is correct!'.format(self.buzzed_in))
            self.solve(self.buzzed_in)
            print('')
        print('Player {} has won!'.format(self.winner()))

    def play_round(self):
        self.trick.cards.append(self.players[0].hand.pop())
        self.trick.cards.append(self.players[0].hand.pop())
        self.trick.cards.append(self.players[1].hand.pop())
        self.trick.cards.append(self.players[1].hand.pop())

    # TODO: implement in main loop.
    def return_cards(self):
        self.players[0].hand.insert(0, self.trick.cards[0])
        self.players[0].hand.insert(0, self.trick.cards[1])
        self.players[1].hand.insert(0, self.trick.cards[2])
        self.players[1].hand.insert(0, self.trick.cards[3])

    def buzz_in(self, player_num):
        self.buzzed_in = player_num

    def is_valid_guess(self, guess):
        is_valid = True

        try:
            eval(guess)
        except Exception:
            is_valid = False
        return is_valid

    def is_correct_guess(self, guess):
        return eval(guess) == 24

    # TODO: implement.
    def is_solvable(self, trick):
        return True

    def solve(self, player_num):
        self.players[player_num].hand.extend(self.trick.cards)
        self.trick.cards = []
        self.players[player_num].points += 1

    def winner(self):
        if len(self.players[0].hand) == 40 or self.players[0].points == 15:
            return 0
        if len(self.players[1].hand) == 40 or self.players[1].points == 15:
            return 1
        return False

if __name__ == '__main__':
    TwentyFourTable().play_game()
