from CardObjects import Card

import gettext
_ = gettext.gettext

class UnoCard(Card):

    def __init__(self, value=None, type=None, color=None):
        if value == None or type == None or color == None \
            or color not in [_('Black'), _('Red'), _('Blue'), _('Green'), _('Yellow')] \
            or type not in [_('Number'), _('Skip'), _('Reverse'), _('Draw Two'), _('Wild')]:
            raise ValueError
        else:
            self.value = value
            self.type = type
            self.color = color

    def __str__(self):
        if self.type is _('Number'):
            return '{} {}'.format(self.color, self.value)
        elif self.type is _('Wild'):
            if self.color != _('Black'):
                return _('{} Wild').format(self.color)
            else:
                return _('Wild Card')
        else:
            return '{} {}'.format(self.color, self.type)

    __repr__ = __str__

    def set_color_of_wild(self, color):
        if color in [_('Red'), _('Blue'), _('Green'), _('Yellow')] and self.type == _('Wild'):
            self.color = color
        else:
            raise ValueError
