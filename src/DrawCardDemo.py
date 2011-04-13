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

        #set up "playing area"
        pygame.draw.rect(self.screen, (0, 0, 255), (500, 300, 75, 100))
        self.screen.blit(self.aFont.render('Deck', 1, (0, 0, 0)), (self.w / 2 - 100, self.h / 2 + 1))
        self.draw_hand_area()

        #set up cards, etc.
        self.table = Table(1)
        
    def draw_card(self, x, y, card):
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 75, 100), 2)
        self.screen.blit(self.aFont.render(str(card), 1, (0, 0, 0)), (x, y))
    
    def draw_hand(self):
        self.draw_hand_area()
        for i, c in enumerate(self.table.players[0].hand):
            self.draw_card(i + i * 100, 640, c)

    def click_is_in(self, xr, yr, pos):
        return pos[0] >= xr[0] and pos[0] <= xr[1] and pos[1] >= yr[0] and pos[1] <= yr[1]

    def draw_hand_area(self):
        pygame.draw.rect(self.screen, (51, 204, 66), (0, 640, self.w, 640))
        pygame.draw.line(self.screen, (0,0,0), (0, 640), (self.w, 640))

    #general pygame stuff
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        if self.click_is_in((500, 575), (300, 400), pos):
            if button == 1:
                self.table.players[0].draw_from(self.table.deck)
                self.draw_hand()
        
    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        pass



s = DrawDemo()
s.mainLoop(40)
