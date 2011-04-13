from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Starter(PygameHelper):
	def __init__(self):
		self.w = 800
		self.h = 600
		PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
		
		self.RGB = (0, 0, 0)
		self.colortab = pygame.image.load("colors.png")
		self.screen.blit(self.colortab, (0,0))
		pygame.draw.line(self.screen, (0,0,0), (0,172), (800,172))
		
		self.x = 0
		
		self.aFont = pygame.font.Font(None, 14)
		text1 = self.aFont.render("Current RGB Value:", 1, (10, 10, 10))
		self.text2 = self.aFont.render("R:%s G:%s B:%s" % (self.RGB[0], self.RGB[1], self.RGB[2]), 1, (10, 10, 10))
		self.screen.blit(text1, (200,60))
		self.screen.blit(self.text2, (200,70))
		
		self.drawCurrColorInfo()

		
		
	def drawCurrColorInfo(self):
		pygame.draw.rect(self.screen, self.RGB, (200,80,30,30))
		pygame.draw.rect(self.screen, (255,255,255), (200,70,100,9))
		self.text2 = self.aFont.render("R:%s G:%s B:%s" % (self.RGB[0], self.RGB[1], self.RGB[2]), 1, (10, 10, 10))
		self.screen.blit(self.text2, (200,70))
	
	#general pygame stuff    
	def update(self):
		pass
        
	def keyUp(self, key):
		pass
        
	def mouseUp(self, button, pos):
		if pos[0] <= 172:
				if button == 1:
					self.RGB = self.screen.get_at(pos)
					self.drawCurrColorInfo()
        
	def mouseMotion(self, buttons, pos, rel):
		if pos[1] > 172:
			if buttons[0] == 1:
				pygame.draw.line(self.screen, self.RGB, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
			elif buttons[2] == 1:
				pygame.draw.circle(self.screen, (255,255,255), pos, 30)
				pygame.draw.line(self.screen, (0,0,0), (0,172), (800,172))
				self.screen.blit(self.colortab, (0,0))
			elif buttons[1] == 1:
				color = self.screen.get_at((self.x, 0))
				pygame.draw.line(self.screen, color, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
				self.x += 1
				if self.x >= 172:
					self.x = 0
		else:
			pass

	def draw(self):
		pass
 
s = Starter()
s.mainLoop(40)
