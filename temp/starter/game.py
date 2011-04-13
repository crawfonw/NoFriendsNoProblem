from pygamehelper import *
from pygame import *
from pygame.locals import *

class Game(PygameHelper):
    
    def __init__(self):
        #general set up
        self.w = 800
        self.h = 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255, 255, 255)), title='Go Fish')
        self.aFont = pygame.font.Font(None, 24)
        pygame.draw.rect(self.screen, (51, 204, 66), (0, 0, self.w, self.h))

        #set up "playing area"
        pygame.draw.rect(self.screen, (0, 0, 0), (200, 200, 75, 100), 2)
        self.screen.blit(self.aFont.render('Deck', 1, (0, 0, 0)), (220, 230))
        pygame.draw.line(self.screen, (0,0,0), (0, 450), (800, 450))







s = Game()
s.mainLoop(40)
