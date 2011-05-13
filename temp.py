import random
from CardObjects import Card

class Deck(object):

    def __init__(self, jokers=False):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for value in range(1, 14):
            for suit in suits:
                self.cards.append(Card(value, suit))
        if jokers:
            self.cards.append(Card(0, "Jokers"))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
from TableObjects import Table
from TwentyFourPlayerObjects import TwentyFourPlayer
from TwentyFourDeckObjects import TwentyFourDeck
from TrickObjects import Trick
import compiler
import itertools
import msvcrt
import time

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
                print('Player {} has {} cards and {} points.'.format(i, len(self.players[i].hand), self.players[i].points))

            print('Make 24 out of these cards:')
            print('   {}'.format(self.trick.cards))

            print('Press any key to buzz in...')
            start_time = time.time()

            while True:
                if msvcrt.kbhit():
                    print 'Human player buzzed in!'
                    self.buzz_in(0)
                    break
                else:
                    if time.time() - start_time > self.timeout:
                        print 'Computer player buzzed in!'
                        self.buzz_in(1)
                        break

            # shouldn't happen with new buzzing system, but just in case...
            if self.buzzed_in != 0 and self.buzzed_in != 1:
                print('Invalid input.')
                continue

            if self.buzzed_in == 0:
                print('What is your guess?')
                guess = raw_input('> ')

                if not self.is_valid_guess(guess):
                    print('Guess is invalid!')
                    continue

                if not self.is_correct_guess(guess):
                    print('That doesn\'t make 24!')
                    continue
            elif self.buzzed_in == 1:
                print 'The computer guessed {}.'.format(self.find_solution())

            print('Player {} is correct!'.format(self.buzzed_in))
            self.solve(self.buzzed_in)
            print('')
        print('Player {} has won!'.format(self.winner()))

    def play_round(self):
        self.trick.cards.append(self.players[0].hand.pop())
        self.trick.cards.append(self.players[0].hand.pop())
        self.trick.cards.append(self.players[1].hand.pop())
        self.trick.cards.append(self.players[1].hand.pop())

    def return_cards(self):
        print "Couldn't find a solution to current trick. Returning cards to players' hands..."
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
from DeckObjects import Deck

class DiscardPile(Deck):
    
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]

    def has_double(self):
        if len(self.cards) > 1:
            return not (self.cards[-1] < self.cards[-2]) and \
                   not (self.cards[-2] < self.cards[-1])
        else:
            return False

    def has_sandwich(self):
        if len(self.cards) > 2:
            return not (self.cards[-1] < self.cards[-3]) and \
                   not (self.cards[-3] < self.cards[-1])
        else:
            return False
import random
from CardObjects import Card
from DeckObjects import Deck

class TwentyFourDeck(Deck):

    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for value in range(1, 11):
            for suit in suits:
                self.cards.append(Card(value, suit))
from TableObjects import Table
from GoFishHumanPlayerObjects import GoFishHumanPlayer
from GoFishAIPlayerObjects import GoFishAIPlayer
from DeckObjects import Deck

class GoFishTable(Table):

    def __init__(self, player_count=2):
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        self.players.append(GoFishHumanPlayer('Puny Human'))
        for i in range(player_count - 1):
            self.players.append(GoFishAIPlayer('AI%s' % (i + 1)))
        self.deal(7)

        #interacting with GUI
        self.current_player = 0
        self.other_player = None

    def get_winner(self):
        max_score_player = -1
        for i in range(len(self.players)):
            if max_score_player == -1 or self.players[i].score > self.players[max_score_player].score:
                max_score_player = i
        return max_score_player
    
    def play_turn(self, card_value=None):
        ret = ''
        others = self.players[0:self.current_player] + self.players[self.current_player+1:]
        print "Player %s:" % self.current_player
        if self.players[self.current_player].player_type() == 1: #is AI
            ret = self.players[self.current_player].play_round(others, self.deck)
        else: #is Human
            ret = self.players[self.current_player].play_round(card_value, self.players, self.other_player, self.deck)
        self.players[self.current_player].update_score()
        self.current_player = (self.current_player + 1) % (len(self.players))
        return ret

    def winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                return True
        return False
from CardObjects import Card

class UnoCard(Card):

    def __init__(self, value=None, type=None, color=None):
        if value == None or type == None or color == None \
            or color not in ['Black', 'Red', 'Blue', 'Green', 'Yellow'] \
            or type not in ['Number', 'Skip', 'Reverse', 'Draw Two', 'Wild']:
            raise ValueError
        else:
            self.value = value
            self.type = type
            self.color = color

    def __str__(self):
        if self.type is 'Number':
            return '%s %s' % (self.color, self.value)
        elif self.type is 'Wild':
            if self.color != 'Black':
                return '%s Wild' % self.color
            else:
                return 'Wild Card'
        else:
            return '%s %s' % (self.color, self.type)

    __repr__ = __str__

    def set_color_of_wild(self, color):
        if color in ['Red', 'Blue', 'Green', 'Yellow'] and self.type == 'Wild':
            self.color = color
        else:
            raise ValueError
from GoFishPlayerObjects import GoFishPlayer
from random import randrange

class GoFishAIPlayer(GoFishPlayer):

    def player_type(self):
        return 1

    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
        except:
            pass

    def take_card(self, other, index):
        ret = "%s takes the %s from %s! The turn is over." % (self, other.hand[index], str(other))
        print ret
        self.hand = self.hand + [other.hand[index]]
        other.hand = other.hand[0:index] + other.hand[index+1:]
        return ret

    def get_best_value(self):
        card_values = [0 for i in range(13)]
        for card in self.hand:
            card_values[card.value - 1] = card_values[card.value - 1] + 1
        try:
            return card_values.index(max(card_values)) + 1
        except:
            return -1

    def play_round(self, others, deck):
        player = randrange(len(others))
        value = self.get_best_value()
        index = others[player].has_card_index(value)
        if index > -1:
            return self.take_card(others[player], index)
        else:
            self.draw_from(deck)
            ret = "%s asks if %s has any %s's, but must fish... Their turn is over." % (self, str(others[player]), value)
            print ret
            return ret

class Card(object):
    
    def __init__(self, value=None, suit=None, name=None):
        if value == None or suit == None or suit == "":
            raise ValueError
        else:
            self.value = value
            self.suit = suit
            if name != None:
                self.name = name
            else:
                self.name = self.get_name()

    def __str__(self):
        if self.value != 0:
            return "%s of %s" % (self.name, self.suit)
        else:
            return self.name

    __repr__ = __str__

    def get_name(self):
        if 1 < self.value <= 10:
            return str(self.value)
        elif self.value == 1:
            return "Ace"
        elif self.value == 11:
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13:
            return "King"
        elif self.value == 0:
            return "Joker"
        else:
            raise ValueError

    def same_as(self, other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        if self.value < other.value:
            return 1
        else:
            return 0
from UnoPlayerObjects import UnoPlayer

class HumanUnoPlayer(UnoPlayer):

    def player_type(self):
        return 0

    def card_index_in_hand(self, card_str):
        for i, c in enumerate(self.hand):
            if card_str == str(c):
                return i
        return -1

    def play_card(self, card_str, pile):
        ret = False
        index = self.card_index_in_hand(card_str)
        if index == -1:
            pass
            #print 'That card is not in your hand!'
        elif self.is_valid_move(self.hand[index], pile.peek()):
            pile.add(self.hand[index])
            self.hand = self.hand[:index] + self.hand[index + 1:]
            ret = True
        else:
            pass
            #print 'That is not a valid move!'

        return ret
from PlayerObjects import Player
from CardObjects import Card

class TwentyFourPlayer(Player):

    def __init__(self):
        self.hand = []
        self.points = 0

from pygamehelper import *
from pygame import *
from pygame.locals import *

from CardObjects import Card
from DeckObjects import Deck
from PlayerObjects import Player
from TableObjects import Table

class DrawDemo(PygameHelper):
    
    def __init__(self):
        #constants: sizes, colors, etc.
        self.w = 1200
        self.h = 800
        self.card_w = 72
        self.card_h = 96

        self.draw_x = 500
        self.draw_y = 300
        self.discard_x = 650
        self.discard_y = 300
        self.hand_area_x = 0
        self.hand_area_y = 640
        
        self.color_background = (51, 204, 66)
        self.color_draw = (0, 0, 255)
        self.color_discard = (255, 0, 0)

        #general set up
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)), title='Go Fish')
        pygame.draw.rect(self.screen, self.color_background, (0, 0, self.w, self.h))
        self.label_font = pygame.font.Font(None, 16)
        self.message_font = pygame.font.Font(None, 20)

        #load card images
        self.clubs = []
        self.diamonds = []
        self.hearts = []
        self.spades = []
        for i in range(1, 14):
            self.clubs.append(pygame.image.load('images/C%s.png' % i))
            self.diamonds.append(pygame.image.load('images/D%s.png' % i))
            self.hearts.append(pygame.image.load('images/H%s.png' % i))
            self.spades.append(pygame.image.load('images/S%s.png' % i))
        self.jokers = [pygame.image.load('images/Z0.png'), pygame.image.load('images/Z1.png')]

        #set up cards, etc.
        self.table = Table(1)

        #set up 'playing area'
        self.draw_deck()
        self.draw_discard()
        self.draw_hand_area()
        self.hand_locs = []
        
    #Screen drawing methods
    def draw_deck_label(self):
        self.screen.blit(self.label_font.render('Deck: %r' % len(self.table.deck.cards), 1, (0, 0, 0)), (self.w / 2 - 100, self.h / 2 + 1))

    def draw_discard_label(self):
        self.screen.blit(self.label_font.render('Discard Pile: %r' % len(self.table.discard.cards), 1, (0, 0, 0)), (self.w / 2 + 50, self.h / 2 + 1))

    def draw_card(self, x, y, card):
        if card.suit == 'Clubs':
            self.screen.blit(self.clubs[card.value - 1], (x, y))
        elif card.suit == 'Diamonds':
            self.screen.blit(self.diamonds[card.value - 1], (x, y))
        elif card.suit == 'Hearts':
            self.screen.blit(self.hearts[card.value - 1], (x, y))
        elif card.suit == 'Spades':
            self.screen.blit(self.spades[card.value - 1], (x, y))
        else:
            self.screen.blit(self.jokers[0], (x, y))
        
        pygame.draw.rect(self.screen, self.color_background, (self.w / 2 - 100, self.h / 2 + 1, 50, 10))
        self.draw_deck_label()

    def draw_deck(self):
        pygame.draw.rect(self.screen, self.color_draw , (self.draw_x, self.draw_y, self.card_w, self.card_h))
        self.draw_deck_label()

    def draw_discard(self, card=None):
        pygame.draw.rect(self.screen, self.color_discard, (self.discard_x, self.discard_y, self.card_w, self.card_h))
        pygame.draw.rect(self.screen, self.color_background, (self.w / 2 + 50, self.h / 2 + 1, 85, 10))
        self.draw_discard_label()

        if card:
            self.draw_card(self.discard_x, self.discard_y, card)

    def draw_hand(self):
        self.hand_locs = []
        self.draw_hand_area()
        for i, c in enumerate(self.table.players[0].hand):
            self.draw_card(i + i * 100, self.hand_area_y, c)
            self.hand_locs.append((i + i * 100, self.hand_area_y))    

    def draw_hand_area(self):
        pygame.draw.rect(self.screen, self.color_background, (self.hand_area_x, self.hand_area_y, self.w, self.hand_area_y))
        pygame.draw.line(self.screen, (0,0,0), (self.hand_area_x, self.hand_area_y), (self.w, self.hand_area_y))

    #click checking
    def click_is_in(self, xr, yr, pos):
        return pos[0] >= xr[0] and pos[0] <= xr[1] and pos[1] >= yr[0] and pos[1] <= yr[1]

    def check_draw_click(self):
        if len(self.table.deck.cards) == 0:
            self.screen.blit(self.message_font.render('No more cards to draw!', 1, (0, 0, 0)), (400, 750))
        elif len(self.table.players[0].hand) < 7:
            self.table.players[0].draw_from(self.table.deck)
            self.draw_hand()
        else:
            self.screen.blit(self.message_font.render('You cannot have more than 7 cards in your hand', 1, (0, 0, 0)), (400, 750))

    def check_discard_click(self, pos):
        temp = None
        for i, loc in enumerate(self.hand_locs):
            if self.click_is_in((loc[0], loc[0] + self.card_w), (loc[1], loc[1] + self.card_w), pos):
                temp = self.table.players[0].hand[i]
                self.table.players[0].hand.remove(temp)
                self.table.discard.add(temp)
        if temp:
            self.draw_hand()
            self.draw_discard(temp)

    #general pygame stuff
    def mouseUp(self, button, pos):
        if button == 1:
            if self.click_is_in((self.draw_x, self.draw_x + self.card_w), (self.draw_y, self.draw_y + self.card_h), pos):
                self.check_draw_click()
            elif pos[1] >= self.hand_area_y and len(self.table.players[0].hand) > 0:
                self.check_discard_click(pos)
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass

    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        pass



s = DrawDemo()
s.mainLoop(40)
from GoFishPlayerObjects import GoFishPlayer

class GoFishHumanPlayer(GoFishPlayer):

    def player_type(self):
        return 0

    def print_hand(self):
        print "Your hand contains: %s" % self.hand

    def take_card(self, other, index):
        ret = "You take the %s!" % other.hand[index]
        self.hand = self.hand + [other.hand[index]]
        other.hand = other.hand[0:index] + other.hand[index+1:]
        print ret
        return ret

    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
            ret = "You got the %s" % self.hand[0]
            return ret
        except:
            ret = "The deck is empty!"
            print ret
            return ret

    def play_round(self, card_value, others, player_id, deck):
        index = others[player_id].has_card_index(card_value)
        if index > -1:
            return self.take_card(others[player_id], index)
        else:
            ret = self.draw_from(deck)
            newret = "Go Fish! - %s" % ret
            print newret
            return newret
import random

from UnoPlayerObjects import UnoPlayer

class AIUnoPlayer(UnoPlayer):

    def player_type(self):
        return 1

    def card_index_in_hand(self, card_str):
        for i, c in enumerate(self.hand):
            if card_str == str(c):
                return i
        return -1

    def play_card(self, card_str, pile):
        ret = False
        index = self.card_index_in_hand(card_str)
        if index == -1:
            print 'That card is not in your hand!'
        elif self.is_valid_move(self.hand[index], pile.peek()):
            pile.add(self.hand[index])
            self.hand = self.hand[:index] + self.hand[index + 1:]
            ret = True
        else:
            print 'That is not a valid move!'

        return ret

    def find_best_move(self, next_player, pile):
        colors = {'Blue':0, 'Green':1, 'Red':2, 'Yellow':3}
        enum_colors, enum_values = self.enumerate_cards()
        top = colors[pile.peek().color]
        hand = str(self.hand)
        move = 'Draw'

        if len(enum_colors[top]) != 0: #play a card via color, highest priority
            move = str(random.choice(enum_colors[top]))

        if len(enum_values[pile.peek().value]) != 0 and move == 'Draw':
            max_colors = 0
            for card in enum_values[pile.peek().value]:
                color_count = len(enum_colors[colors[card.color]])
                if color_count > max_colors:
                    max_colors = color_count
                    move = str(card)

        if 'Skip' in hand: #a skip?
            if len(next_player.hand) < 4 or move == 'Draw':
                if '%s Skip' % pile.peek().color in hand:
                    move = '%s Skip' % pile.peek().color
                elif pile.peek().type == 'Skip':
                    move = self.find_correct_color_card_combination(colors.keys(), 'Skip')
        if 'Draw Two' in hand: #a draw two?
            if len(next_player.hand) < 4 or move == 'Draw':
                if '%s Draw Two' % pile.peek().color in hand:
                    move = '%s Draw Two' % pile.peek().color
                elif pile.peek().type == 'Draw Two':
                    move = self.find_correct_color_card_combination(colors.keys(), 'Draw Two')
        if 'Reverse' in hand: #a reverse?
            if len(next_player.hand) < 4 or move == 'Draw':
                if '%s Reverse' % pile.peek().color in hand:
                    move = '%s Reverse' % pile.peek().color
                elif pile.peek().type == 'Reverse':
                    move = self.find_correct_color_card_combination(colors.keys(), 'Reverse')
        if 'Wild Card' in hand and move == 'Draw': #if we have a wild, should we play it?
            index = self.card_index_in_hand('Wild Card')
            self.hand[index].set_color_of_wild(self.find_max_colors())
            move = str(self.hand[index])
        return move

    def find_correct_color_card_combination(self, color_keys, card_type):
        for color in color_keys:
            s = '%s %s' % (color, card_type)
            if self.card_index_in_hand(s) != -1:
                return s

    def enumerate_cards(self):
        colors = [[], [], [], []] #blue, green, red, yellow
        values = [[], [], [], [], [], [], [], [], [], [], []]
        for card in self.hand:
            if card.value > -1:
                values[card.value].append(card)
                if card.color == 'Blue':
                    colors[0].append(card)
                elif card.color == 'Green':
                    colors[1].append(card)
                elif card.color == 'Red':
                    colors[2].append(card)
                elif card.color == 'Yellow':
                    colors[3].append(card)
        return colors, values

    def find_max_colors(self):
        max_list = []
        colors = [[], [], [], []]
        for card in self.hand:
            if card.color == 'Blue':
                colors[0].append(card)
            elif card.color == 'Green':
                colors[1].append(card)
            elif card.color == 'Red':
                colors[2].append(card)
            elif card.color == 'Yellow':
                colors[3].append(card)
        for l in colors:
            if len(l) > len(max_list):
                max_list = l
        if len(max_list) == 0:
            return random.choice(['Blue', 'Green', 'Red', 'Yellow'])
        return max_list[0].color
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


import unittest

from CardTests import *
from DeckTests import *
from DiscardPileTests import *
from PlayerTests import *
from TableTests import *
from GoFishTableTests import *
from GoFishPlayerTests import *
from GoFishHumanPlayerTests import *
from GoFishAIPlayerTests import *

from GoFishPlayerTests import *
from GoFishTableTests import *

#from SlapJackPlayerTests import *
#from SlapJackTableTests import *

from TwentyFourTests import *

load = unittest.TestLoader().loadTestsFromTestCase

suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable, TestGoFishTable, TestGoFishPlayer, TestGoFishHumanPlayer, TestGoFishAIPlayer, TestTwentyFour])

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
from CardObjects import Card

class Trick(object):

    def __init__(self):
        self.cards = []
from DeckObjects import Deck

class Player(object):
    
    def __init__(self, name = ''):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name
        
    def draw_from(self, deck):
        try:
            self.hand.insert(0, deck.draw())
        except:
            pass

    def has_card_index(self, value):
        for i in range(len(self.hand)):
            if self.hand[i].value == value:
                return i
        return -1

    def play_card(self):
        return self.hand.pop()
from PlayerObjects import Player
from CardObjects import Card

class ERSPlayer(Player):
    
    def __init__(self):
        pass

    def flip(self):
        pass

    def slap(self, card):
        pass
from pygamehelper import *
from pygame import *
from pygame.locals import *

from CardObjects import Card
from DeckObjects import Deck

from GoFishTableObjects import GoFishTable

class GoFishGUI(PygameHelper):
    
    def __init__(self):
        #constants: sizes, colors, etc.
        self.w = 1200
        self.h = 800
        self.card_w = int(72 / 1.5)
        self.card_h = int(96 / 1.5)
        self.turn_button_dim = (65, 15)
        self.card_spacing = self.card_h

        self.deck_x = 500
        self.deck_y = 300
        self.hand_area_x = 0
        self.hand_area_y = 640
        self.message_x = 400
        self.message_y = 750
        self.score_x = 0
        self.score_y = 0
        self.selected_player = (0, 20)
        self.turn_label = (0, 40)
        self.turn_button = (0, 60)
        
        self.color_background = (51, 204, 66)
        self.color_draw = (0, 0, 255)
        self.color_next = (255, 0, 0)

        #general set up
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)), title='Go Fish')
        pygame.draw.rect(self.screen, self.color_background, (0, 0, self.w, self.h))
        self.label_font = pygame.font.Font(None, 18)
        self.message_font = pygame.font.Font(None, 20)

        #load card images
        self.clubs = []
        self.diamonds = []
        self.hearts = []
        self.spades = []
        for i in range(1, 14):
            self.clubs.append(pygame.transform.scale(pygame.image.load('images/C%s.png' % i), (self.card_w, self.card_h)))
            self.diamonds.append(pygame.transform.scale(pygame.image.load('images/D%s.png' % i), (self.card_w, self.card_h)))
            self.hearts.append(pygame.transform.scale(pygame.image.load('images/H%s.png' % i), (self.card_w, self.card_h)))
            self.spades.append(pygame.transform.scale(pygame.image.load('images/S%s.png' % i), (self.card_w, self.card_h)))
        self.jokers = [pygame.transform.scale(pygame.image.load('images/Z0.png'), (self.card_w, self.card_h)), pygame.transform.scale(pygame.image.load('images/Z1.png'), (self.card_w, self.card_h))]

        #set up cards, etc.
        self.IS_AI_TURN = False
        self.TURN_IS_DONE = False
        self.table = GoFishTable(4)

        #set up 'playing area'
        self.hand_locs = []
        self.draw_all()

    #Screen drawing methods
    def draw_all(self):
        self.draw_deck()
        self.draw_hand_area()
        self.draw_hand()
        self.draw_score()
        self.draw_selected_player()
        self.draw_turn_label()
        self.draw_turn_button()

    def draw_score(self):
        score_text = 'Scores: '
        for player in self.table.players:
            score_text += '%s: %s ' % (player, player.score)
        pygame.draw.rect(self.screen, self.color_background, (self.score_x, self.score_y, self.w, 15))
        self.screen.blit(self.message_font.render(score_text, 1, (0, 0, 0)), (self.score_x, self.score_y))

    def draw_selected_player(self):
        if self.table.other_player:
            sel = 'Selected Opponent: %s' % self.table.players[self.table.other_player]
        else:
            sel = 'Selected Opponent: None'
        pygame.draw.rect(self.screen, self.color_background, (self.selected_player[0], self.selected_player[1], self.w, 15))
        self.screen.blit(self.message_font.render(sel, 1, (0, 0, 0)), (self.selected_player[0], self.selected_player[1]))

    def draw_message(self, message):
        pygame.draw.rect(self.screen, self.color_background, (0, self.message_y, self.w, 15))
        self.screen.blit(self.message_font.render(message, 1, (0, 0, 0)), (self.message_x, self.message_y))

    def draw_turn_button(self):
        pygame.draw.rect(self.screen, self.color_next, (self.turn_button[0], self.turn_button[1], self.turn_button_dim[0], self.turn_button_dim[1]))
        self.screen.blit(self.message_font.render('Next Turn', 1, (0, 0, 0)), (self.turn_button[0] + 2, self.turn_button[1] + 2))

    def draw_turn_label(self):
        text = "It is %s's turn." % self.table.players[self.table.current_player]
        pygame.draw.rect(self.screen, self.color_background, (self.turn_label[0], self.turn_label[1], self.w, 15))
        self.screen.blit(self.message_font.render(text, 1, (0, 0, 0)), (self.turn_label[0], self.turn_label[1]))

    def draw_deck_label(self):
        pygame.draw.rect(self.screen, self.color_background, (self.w / 2 - 100, self.h / 2 + 1, 50, 10))
        self.screen.blit(self.label_font.render('Deck: %r' % len(self.table.deck.cards), 1, (0, 0, 0)), (self.deck_x, self.deck_y + self.card_spacing))

    def draw_deck(self):
        pygame.draw.rect(self.screen, self.color_draw , (self.deck_x, self.deck_y, self.card_w, self.card_h))
        self.draw_deck_label()

    def draw_card(self, x, y, card):
        if card.suit == 'Clubs':
            self.screen.blit(self.clubs[card.value - 1], (x, y))
        elif card.suit == 'Diamonds':
            self.screen.blit(self.diamonds[card.value - 1], (x, y))
        elif card.suit == 'Hearts':
            self.screen.blit(self.hearts[card.value - 1], (x, y))
        elif card.suit == 'Spades':
            self.screen.blit(self.spades[card.value - 1], (x, y))
        else:
            self.screen.blit(self.jokers[0], (x, y))
        
        self.draw_deck_label()

    def draw_hand(self):
        self.hand_locs = []
        self.draw_hand_area()
        for i, c in enumerate(self.table.players[0].hand):
            self.draw_card(i + i * self.card_spacing, self.hand_area_y, c)
            self.hand_locs.append((i + i * self.card_spacing, self.hand_area_y))    

    def draw_hand_area(self):
        pygame.draw.rect(self.screen, self.color_background, (self.hand_area_x, self.hand_area_y, self.w, self.hand_area_y))
        pygame.draw.line(self.screen, (0,0,0), (self.hand_area_x, self.hand_area_y), (self.w, self.hand_area_y))

    #click checking
    def click_is_in(self, xr, yr, pos):
        return pos[0] >= xr[0] and pos[0] <= xr[1] and pos[1] >= yr[0] and pos[1] <= yr[1]

    def check_draw_click(self):
        if len(self.table.deck.cards) == 0:
            self.draw_message('No more cards to draw!')

    def click_is_in_hand(self, pos):
        print
        for p in self.table.players:
            print '%s: %s' % (p, p.hand)
        print
        message = ''
        temp = None
        for i, loc in enumerate(self.hand_locs):
            if self.click_is_in((loc[0], loc[0] + self.card_w), (loc[1], loc[1] + self.card_w), pos):
                temp = self.table.players[0].hand[i]
        if temp:
            if not self.table.other_player:
                message = 'Choose a player to take a card from!'
            else:
                message = self.table.play_turn(temp.value)
                self.TURN_IS_DONE = True
                self.IS_AI_TURN = True

            #redraw stuff
            self.draw_all()
            self.draw_message(message)

    #general pygame stuff
    def mouseUp(self, button, pos):
        if not self.table.winner():
            if button == 1:
                self.draw_all()
                if self.click_is_in((self.turn_button[0], self.turn_button[0] + self.turn_button_dim[0]) , (self.turn_button[1], self.turn_button[1] + self.turn_button_dim[1]), pos) and self.TURN_IS_DONE:
                    self.draw_turn_label()
                    if self.IS_AI_TURN: #an AI player's turn
                        msg = self.table.play_turn() #no args for AI player
                        self.draw_message(msg)
                        self.TURN_IS_DONE = True
                        if self.table.current_player == 0:
                            self.IS_AI_TURN = False
                    else:
                        self.TURN_IS_DONE = False #Human player's turn
                elif not self.TURN_IS_DONE:
                    if self.click_is_in((self.deck_x, self.deck_x + self.card_w), (self.deck_y, self.deck_y + self.card_h), pos): #check if drawing a card
                        self.check_draw_click()
                    elif pos[1] >= self.hand_area_y and len(self.table.players[0].hand) > 0 and self.table.current_player == 0: #check if clicking card in hand
                        self.click_is_in_hand(pos)
                else:
                    self.draw_message('The turn is over! Please press the next button.')
        else:
            winner = self.table.players[self.table.get_winner()]
            self.draw_message('%s is the winner with %s matches!' % (winner, winner.score))
        
    def update(self):
        pass
        
    def keyUp(self, key):
        if key >= 49 and key <= 57: #key pressed is 1 - 9
            delta = key - 48
            if len(self.table.players) - 1 < delta:
                self.draw_message("You don't have that many opponents!")
            else:
                self.table.other_player = delta
                self.draw_all()
                self.draw_message('You have selected opponent %s' % self.table.players[delta])

    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        pass



s = GoFishGUI()
s.mainLoop(40)
from PlayerObjects import Player

class UnoPlayer(Player): 

    def hand_is_empty(self):
        return len(self.hand) == 0

    def is_valid_move(self, card, top):
        return card.type == 'Wild' or \
                top.type == 'Wild' or \
                card.value == top.value or \
                card.color == top.color or \
                (card.type == 'Skip' and top.type == 'Skip') or \
                (card.type == 'Reverse' and top.type == 'Reverse') or \
                (card.type == 'Draw Two' and top.type == 'Draw Two')

    def play_card(self, card, pile):
        pass

    def print_hand(self):
        s = ''
        for card in self.hand:
            s += str(card)
        print 'Your hand contains:\n%s\n' % s
import random
from UnoCardObjects import UnoCard
from DeckObjects import Deck

class UnoDeck(Deck):

    def __init__(self):
        self.cards = []
        colors = ['Blue', 'Green', 'Red', 'Yellow']
        for value in range(0, 10):
            for color in colors:
                self.cards.append(UnoCard(value, 'Number', color))
                self.cards.append(UnoCard(value, 'Number', color))

        types = ['Draw Two', 'Reverse', 'Skip']
        for color in colors:
            for t in types:
                for value in range(2):
                    self.cards.append(UnoCard(-1, t, color))

        for i in range(4):
            self.cards.append(UnoCard(-1, 'Wild', 'Black'))
from PlayerObjects import Player
from CardObjects import Card

class GoFishPlayer(Player):

    def __init__(self, name = ''):
        self.hand = []
        self.score = 0
        self.name = name

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
        pass

    def draw_from(self, deck):
        pass

    def play_round(self, others, deck):
        pass

    def player_type(self):
        pass
from TableObjects import Table
from ERSPlayerObjects import ERSPlayer
from DiscardPileObjects import DiscardPile
from DeckObjects import Deck

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
        pass

    def play_game(self):
        pass

    def winner(self):
        pass
from DiscardPileObjects import DiscardPile
from TableObjects import Table

from UnoDeckObjects import UnoDeck
from UnoHumanPlayerObjects import HumanUnoPlayer
from UnoAIPlayerObjects import AIUnoPlayer

class UnoTable(Table):

    def __init__(self, player_count = 2):
        self.players = []
        self.deck = UnoDeck()
        self.deck.shuffle()
        self.discard = DiscardPile()
        self.players.append(HumanUnoPlayer('Human 1'))
        for i in range(player_count - 1):
            self.players.append(AIUnoPlayer('Computer %s' % (i + 1)))

        self.deal(7)
        self.current_player = 0
        self.TURN_CONS = 1

        self.play_game()

    def get_winner(self):
        return self.winner()

    def play_game(self):
        self.shuffle_and_turn()
        while not self.winner():
            result = None
            if len(self.deck.cards) == 0:
                self.shuffle_and_turn()
            print "\n~~~~~%s's Turn~~~~~\n" % self.players[self.current_player]
            if self.players[self.current_player].player_type() == 1: #is AI
                move = self.players[self.current_player].find_best_move(self.players[(self.current_player + self.TURN_CONS) % (len(self.players))], self.discard)
                if move == 'Draw':
                    print '%s draws a card...' % (self.players[self.current_player])
                    self.players[self.current_player].draw_from(self.deck)
                    result = 'draw'
                else:
                    print '%s plays a %s' % (self.players[self.current_player], move)
                    result = self.players[self.current_player].play_card(move, self.discard)
            else: #is Human
                print '+==================================+\n| Cards in deck: %s' % len(self.deck.cards)
                print '| Top of the discard pile: %s\n|' % self.discard.peek()
                print '%s' % self.print_hand_count()
                print '+==================================+\n'
                print '***Your hand contains***\n%s\n' % self.players[self.current_player].hand
                move = raw_input('Please input your move, or draw:\n')
                if move.lower().strip() == 'draw': #draw a card
                    self.players[self.current_player].draw_from(self.deck)
                    print 'You draw a %s' % self.players[self.current_player].hand[0]
                    result = 'draw'
                else: #play a card
                    result = self.players[self.current_player].play_card(move, self.discard)
                    if not result:
                        print 'That is not a valid card/move!\n'
                    else:
                        print '\n%s plays a %s' % (self.players[self.current_player], move)
            if result:
                if len(self.players[self.current_player].hand) == 1:
                    print '^^^^^ %s says UNO! ^^^^^' % self.players[self.current_player]
                self.determine_next_turn(move)
        print '%s wins!' % self.get_winner()

    def winner(self):
        for i, player in enumerate(self.players):
            if len(player.hand) == 0:
                return player

    def determine_next_turn(self, move):
        if 'Skip' in move:
            self.current_player = (self.current_player + 2 * self.TURN_CONS) % (len(self.players))
        elif 'Draw Two' in move:
            self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))
            self.players[self.current_player].draw_from(self.deck)
            self.players[self.current_player].draw_from(self.deck)
        elif 'Reverse' in move:
            self.TURN_CONS *= -1
            self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))
        elif 'Wild' in move and self.players[self.current_player].player_type() == 0:
            valid_color = False
            while not valid_color:
                color = raw_input('Please input the color for the wild card.\n')
                if color in ['Red', 'Blue', 'Green', 'Yellow']:
                    valid_color = True
                    self.discard.peek().set_color_of_wild(color)
                    self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))
        else:
            self.current_player = (self.current_player + self.TURN_CONS) % (len(self.players))

    def shuffle_and_turn(self):
        self.deck.cards.extend(self.discard.cards)
        self.discard.cards = []
        self.deck.shuffle()
        self.discard.add(self.deck.draw())

    def print_hand_count(self):
        s = ''
        for p in self.players:
            s += '| %s has %s cards in hand.\n' % (p, len(p.hand))
        return s.strip()




import pygame
from pygame.locals import *

#float range. Start=a, End=b, Step=c
def frange(a, b, c):
    t = a
    while t < b:
        yield t
        t += c

def drawGraph(screen, arr, step=5):
        maxy = screen.get_height()
        for i in range(len(arr)-1):
            x = i*step
            p1 = (i*step, maxy-arr[i])
            p2 = ((i+1)*step, maxy-arr[i+1])
            pygame.draw.line(screen, (0,0,0), p1, p2)
        
class PygameHelper:
    def __init__(self, size=(640,480), fill=(255,255,255), title='PyGame'):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(fill)
        pygame.display.flip()
        self.running = False
        self.clock = pygame.time.Clock() #to track FPS
        self.size = size
        self.fps= 0
        self.title = title
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                self.keyDown(event.key)
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.running = False
                self.keyUp(event.key)
            elif event.type == MOUSEBUTTONUP:
                self.mouseUp(event.button, event.pos)
            elif event.type == MOUSEMOTION:
                self.mouseMotion(event.buttons, event.pos, event.rel)
    
    #wait until a key is pressed, then return
    def waitForKey(self):
        press=False
        while not press:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    press = True
             
    #enter the main loop, possibly setting max FPS
    def mainLoop(self, fps=0):
        self.running = True
        self.fps= fps
        
        while self.running:
            pygame.display.set_caption("%s: (FPS: %i)" % (self.title, self.clock.get_fps()))
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
    def update(self):
        pass
        
    def draw(self):
        pass
        
    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass
    
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass
