import gettext

# make _ accessible to all modules
import __builtin__
# TODO: insert logic for choosing language
__builtin__._ = gettext.GNUTranslations(open("languages/spanish.mo", "rb")).ugettext # ugettext for unicode
#__builtin__._ = lambda x :x

# TODO: insert "game launcher" logic here
#from TwentyFourTableObjects import TwentyFourTable
#TwentyFourTable().play_game()

#from UnoTableObjects import UnoTable
#UnoTable().play_game()

#from GoFishGUI import *

#from UnoTestSuite import *

#from ERSTableObjects import *
#ERSTable().play_game()

#from OldMaidTableObjects import OldMaidTable
#OldMaidTable().play_game()
