from TableObjects import Table
from TwentyFourPlayerObjects import TwentyFourPlayer
from TwentyFourDeckObjects import TwentyFourDeck
from TrickObjects import Trick
import compiler
import itertools
import os
if os.name == 'nt':
    import msvcrt
    import time
else:
    import sys
    from select import select


class TimeoutException(Exception):
    pass

class TwentyFourTable(Table):
    def __init__(self):
        self.players = []
        for i in [0, 1]:
            self.players.append(TwentyFourPlayer())

        self.trick = Trick()

        self.deck = TwentyFourDeck()
        self.deck.shuffle()
        self.deal(20)

        self.timeout = 10       # lower timeout implies higher difficulty

    def play_game(self):
        def timeout_handler(signum, frame):
            raise TimeoutException()

        while not self.winner():
            if len(self.trick.cards) == 0:
                self.play_round()

            if not self.find_solution():
                self.return_cards()
                continue

            for i in [0, 1]:
                print(_('Player {} has {} cards and {} points.').format(i, len(self.players[i].hand), self.players[i].points))

            print(_('Make 24 out of these cards:'))
            print('   {}'.format(self.trick.cards))

            print(_('Press any key to buzz in...'))

            if os.name == 'nt':
                start_time = time.time()
                while True:
                    if msvcrt.kbhit():
                        print(_('Human player buzzed in!'))
                        self.buzz_in(0)
                        break
                    else:
                        if time.time() - start_time > self.timeout:
                            print(_('Computer player buzzed in!'))
                            self.buzz_in(1)
                            break
            else:
                rlist, __, __ = select([sys.stdin], [], [], self.timeout)
                if rlist:
                    sys.stdin.readline()
                    print(_('Human player buzzed in!'))
                    self.buzz_in(0)
                else:
                    print(_('Computer player buzzed in!'))
                    self.buzz_in(1)

            # shouldn't happen with new buzzing system, but just in case...
            if self.buzzed_in != 0 and self.buzzed_in != 1:
                print(_('Invalid input.'))
                continue

            if self.buzzed_in == 0:
                print(_('What is your guess?'))
                guess = raw_input('> ')

                if not self.is_valid_guess(guess):
                    print(_('Guess is invalid!'))
                    continue

                if not self.is_correct_guess(guess):
                    print(_('That doesn\'t make 24!'))
                    continue
            elif self.buzzed_in == 1:
                print(_('The computer guessed {}.').format(self.find_solution()))

            # print(_('Player {} is correct!').format(self.buzzed_in))
            self.solve(self.buzzed_in)
            print('')
        print(_('Player {} has won!').format(self.winner()))

    def play_round(self):
        self.trick.cards.append(self.players[0].hand.pop())
        self.trick.cards.append(self.players[0].hand.pop())
        self.trick.cards.append(self.players[1].hand.pop())
        self.trick.cards.append(self.players[1].hand.pop())

    def return_cards(self):
        print(_("Couldn't find a solution to current trick. Returning cards to players' hands..."))
        self.players[0].hand.insert(0, self.trick.cards[0])
        self.players[0].hand.insert(0, self.trick.cards[1])
        self.players[1].hand.insert(0, self.trick.cards[2])
        self.players[1].hand.insert(0, self.trick.cards[3])
        self.trick = Trick()

    def buzz_in(self, player_num):
        self.buzzed_in = player_num

    # Test for syntactical correctness.
    # FIXME: Some valid formulae are throwing false negatives.
    def is_valid_guess(self, guess):
        is_valid = True

        try:
            ast = compiler.parse(guess)
        except SyntaxError:
            is_valid = False
        return is_valid

    # Test for legal usage of cards.
    # Fails if guess does not use each number in the trick exactly once.
    # Fails if guess uses an illegal operator (legal operators are +, -, *, /, (, and ).
    def is_legal_guess(self, guess):
        guess_numbers = []
        trick_numbers = map(lambda card: str(card.value), self.trick.cards)
        valid_operators = ['+', '-', '*', '/', '(', ')']

        for c in guess:
            if c.isdigit():
                # print "Adding {} to list of numbers.".format(c)
                guess_numbers.append(c)
            elif c in valid_operators:
                # print "Skipping over operator {}.".format(c)
                continue
            elif c.isspace():
                # print "Skipping over a space."
                continue
            else:
                # print "Found invalid character {}!".format(c)
                return False

        if sorted(guess_numbers) != sorted(trick_numbers):
            # print "Mismatched numbers!"
            return False

        return True

    def is_correct_guess(self, guess):
        return eval(guess) == 24

    # FIXME: eliminate integer division from solutions.
    def find_solution(self):
        for c in itertools.permutations(self.trick.cards):
            for o in itertools.permutations(["+", "-", "*", "/"]):
                guess = str(c[0].value)
                for i in range(3):
                    guess += o[i] + str(c[i+1].value)
                if eval(guess) == 24:
                    return guess
        return False

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

