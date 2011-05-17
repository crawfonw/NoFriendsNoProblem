import gettext

# make _ accessible to all modules
import __builtin__
__builtin__._ = gettext.GNUTranslations(open("languages/spanish.mo", "rb")).ugettext # ugettext for unicode

# insert "game launcher" logic here
from TwentyFourTableObjects import TwentyFourTable
TwentyFourTable().play_game()
