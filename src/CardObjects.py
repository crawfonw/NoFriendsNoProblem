
class Card(object):
    
    def __init__(self, value=None, suit=None, name=None):
        
        if value == None or suit == None or suit == "":
            raise ValueError
        else:
            self.value = value
            self.suit = suit
            if name != None:
                self.name = name
            else:
                self.name = self.get_name()

    def __str__(self):
        if self.value != 0:
            return "%s of %s" % (self.name, self.suit)
        else:
            return self.name

    __repr__ = __str__

    def get_name(self):
        if 1 < self.value <= 10:
            return str(self.value)
        elif self.value == 1:
            return "Ace"
        elif self.value == 11:
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13:
            return "King"
        elif self.value == 0:
            return "Joker"
        else:
            raise ValueError

    def same_as(self, other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        if self.value < other.value:
            return 1
        else:
            return -1
