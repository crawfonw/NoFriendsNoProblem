from pygamehelper import *
from pygame import *
from pygame.locals import *

from CardObjects import Card
from DeckObjects import Deck
from PlayerObjects import Player
from TableObjects import Table

class DrawDemo(PygameHelper):
    
    def __init__(self):
        #general set up
        self.w = 1200
        self.h = 800
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)), title='Go Fish')
        self.aFont = pygame.font.Font(None, 16)
        pygame.draw.rect(self.screen, (51, 204, 66), (0, 0, self.w, self.h))

        #set up cards, etc.
        self.table = Table(1)

        #set up "playing area"
        pygame.draw.rect(self.screen, (0, 0, 255), (500, 300, 75, 100))
        self.screen.blit(self.aFont.render('Deck: %r' % len(self.table.deck.cards), 1, (0, 0, 0)), (self.w / 2 - 100, self.h / 2 + 1))
        self.draw_discard()
        self.draw_hand_area()
        self.hand_locs = []
        
    def draw_card(self, x, y, card):
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 75, 100), 2)
        self.screen.blit(self.aFont.render(str(card), 1, (0, 0, 0)), (x, y))

        pygame.draw.rect(self.screen, (51, 204, 66), (self.w / 2 - 100, self.h / 2 + 1, 50, 10))
        self.screen.blit(self.aFont.render('Deck: %r' % len(self.table.deck.cards), 1, (0, 0, 0)), (self.w / 2 - 100, self.h / 2 + 1))       

    def draw_hand(self):
        self.hand_locs = []
        self.draw_hand_area()
        for i, c in enumerate(self.table.players[0].hand):
            self.draw_card(i + i * 100, 640, c)
            self.hand_locs.append((i + i * 100, 640))

    def click_is_in(self, xr, yr, pos):
        return pos[0] >= xr[0] and pos[0] <= xr[1] and pos[1] >= yr[0] and pos[1] <= yr[1]

    def draw_hand_area(self):
        pygame.draw.rect(self.screen, (51, 204, 66), (0, 640, self.w, 640))
        pygame.draw.line(self.screen, (0,0,0), (0, 640), (self.w, 640))

    def draw_discard(self, card=None):
        pygame.draw.rect(self.screen, (51, 204, 66), (650, 300, 100, 100)) #remove later
        pygame.draw.rect(self.screen, (255, 0, 0), (650, 300, 75, 100))
        pygame.draw.rect(self.screen, (51, 204, 66), (self.w / 2 + 50, self.h / 2 + 1, 85, 10))
        self.screen.blit(self.aFont.render('Discard Pile: %r' % len(self.table.discard.cards), 1, (0, 0, 0)), (self.w / 2 + 50, self.h / 2 + 1))
        if card:
            self.draw_card(650, 300, card)

    #general pygame stuff
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        if self.click_is_in((500, 575), (300, 400), pos):
            if button == 1:
                if len(self.table.deck.cards) == 0:
                    self.screen.blit(self.aFont.render('No more cards to draw!', 1, (0, 0, 0)), (400, 750))
                elif len(self.table.players[0].hand) < 7:
                    self.table.players[0].draw_from(self.table.deck)
                    self.draw_hand()
                else:
                    self.screen.blit(self.aFont.render('You cannot have more than 7 cards in your hand', 1, (0, 0, 0)), (400, 750))
        elif pos[1] >= 640 and len(self.table.players[0].hand) > 0:
            temp = []
            for i, loc in enumerate(self.hand_locs):
                if self.click_is_in((loc[0], loc[0] + 75), (loc[1], loc[1] + 75), pos):
                    temp = self.table.players[0].hand[i]
                    self.table.players[0].hand.remove(temp)
                    self.table.discard.add(temp)
            self.draw_hand()
            self.draw_discard(temp)
        
    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        pass



s = DrawDemo()
s.mainLoop(40)
