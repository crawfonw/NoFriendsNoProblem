from pygamehelper import *
from pygame import *
from pygame.locals import *

from CardObjects import Card
from DeckObjects import Deck

from GoFishTableObjects import GoFishTable

import gettext
_ = gettext.GNUTranslations(open("locales/sp/GoFishSpanish.mo", "rb")).ugettext

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
        score_text = _('Scores: ')
        for player in self.table.players:
            score_text += _('%s: %s ') % (player, player.score)
        pygame.draw.rect(self.screen, self.color_background, (self.score_x, self.score_y, self.w, 15))
        self.screen.blit(self.message_font.render(score_text, 1, (0, 0, 0)), (self.score_x, self.score_y))

    def draw_selected_player(self):
        if self.table.other_player:
            sel = _('Selected Opponent: %s') % self.table.players[self.table.other_player]
        else:
            sel = _('Selected Opponent: None')
        pygame.draw.rect(self.screen, self.color_background, (self.selected_player[0], self.selected_player[1], self.w, 15))
        self.screen.blit(self.message_font.render(sel, 1, (0, 0, 0)), (self.selected_player[0], self.selected_player[1]))

    def draw_message(self, message):
        pygame.draw.rect(self.screen, self.color_background, (0, self.message_y, self.w, 15))
        self.screen.blit(self.message_font.render(message, 1, (0, 0, 0)), (self.message_x, self.message_y))

    def draw_turn_button(self):
        pygame.draw.rect(self.screen, self.color_next, (self.turn_button[0], self.turn_button[1], self.turn_button_dim[0], self.turn_button_dim[1]))
        self.screen.blit(self.message_font.render(_('Next Turn'), 1, (0, 0, 0)), (self.turn_button[0] + 2, self.turn_button[1] + 2))

    def draw_turn_label(self):
        text = _("It is %s's turn.") % self.table.players[self.table.current_player]
        pygame.draw.rect(self.screen, self.color_background, (self.turn_label[0], self.turn_label[1], self.w, 15))
        self.screen.blit(self.message_font.render(text, 1, (0, 0, 0)), (self.turn_label[0], self.turn_label[1]))

    def draw_deck_label(self):
        pygame.draw.rect(self.screen, self.color_background, (self.w / 2 - 100, self.h / 2 + 1, 50, 10))
        self.screen.blit(self.label_font.render(_('Deck: %r') % len(self.table.deck.cards), 1, (0, 0, 0)), (self.deck_x, self.deck_y + self.card_spacing))

    def draw_deck(self):
        pygame.draw.rect(self.screen, self.color_draw , (self.deck_x, self.deck_y, self.card_w, self.card_h))
        self.draw_deck_label()

    def draw_card(self, x, y, card):
        if card.suit == _('Clubs'):
            self.screen.blit(self.clubs[card.value - 1], (x, y))
        elif card.suit == _('Diamonds'):
            self.screen.blit(self.diamonds[card.value - 1], (x, y))
        elif card.suit == _('Hearts'):
            self.screen.blit(self.hearts[card.value - 1], (x, y))
        elif card.suit == _('Spades'):
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
            self.draw_message(_('No more cards to draw!'))

    def click_is_in_hand(self, pos):
        print
        for p in self.table.players:
            print _('%s: %s') % (p, p.hand)
        print
        message = ''
        temp = None
        for i, loc in enumerate(self.hand_locs):
            if self.click_is_in((loc[0], loc[0] + self.card_w), (loc[1], loc[1] + self.card_w), pos):
                temp = self.table.players[0].hand[i]
        if temp:
            if not self.table.other_player:
                message = _('Choose a player to take a card from!')
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
                    self.draw_message(_('The turn is over! Please press the next button.'))
        else:
            winner = self.table.players[self.table.get_winner()]
            self.draw_message(_('%s is the winner with %s matches!') % (winner, winner.score))
        
    def update(self):
        pass
        
    def keyUp(self, key):
        if key >= 49 and key <= 57: #key pressed is 1 - 9
            delta = key - 48
            if len(self.table.players) - 1 < delta:
                self.draw_message(_("You don't have that many opponents!"))
            else:
                self.table.other_player = delta
                self.draw_all()
                self.draw_message(_('You have selected opponent %s') % self.table.players[delta])

    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        pass



s = GoFishGUI()
s.mainLoop(40)
