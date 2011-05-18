import random
from UnoCardObjects import UnoCard
from DeckObjects import Deck

import gettext
_ = gettext.GNUTranslations(open("locales/sp/UnoSpanish.mo", "rb")).ugettext

class UnoDeck(Deck):

    def __init__(self):
        self.cards = []
        colors = [_('Blue'), _('Green'), _('Red'), _('Yellow')]
        for value in range(0, 10):
            for color in colors:
                self.cards.append(UnoCard(value, 'Number', color))
                self.cards.append(UnoCard(value, 'Number', color))

        types = [_('Draw Two'), _('Reverse'), _('Skip')]
        for color in colors:
            for t in types:
                for value in range(2):
                    self.cards.append(UnoCard(-1, t, color))

        for i in range(4):
            self.cards.append(UnoCard(-1, _('Wild'), _('Black')))
