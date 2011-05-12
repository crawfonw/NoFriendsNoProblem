from CardObjects import Card

class UnoCard(Card):

    def __init__(self, value=None, card_type=None, color=None):
        if value == None or card_type == None or color == None \
            or color not in ['Black', 'Red', 'Blue', 'Green', 'Yellow'] \
            or card_type not in ['Number', 'Skip', 'Reverse', 'Draw Two', 'Wild']:
            raise ValueError
        else:
            self.value = value
            self.card_type = card_type
            self.color = color

    def __str__(self):
        if self.card_type is 'Number':
            return '%s %s' % (self.color, self.value)
        elif self.card_type is 'Wild':
            return 'Wild Card'
        else:
            return '%s %s' % (self.color, self.card_type)

    __repr__ = __str__
