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
