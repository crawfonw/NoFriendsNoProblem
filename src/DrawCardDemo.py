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
