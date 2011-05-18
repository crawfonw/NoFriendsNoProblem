import gettext

# make _ accessible to all modules
import __builtin__

# logic for choosing language
print 'Choose a language:'
print '1. English'
print '2. Spanish'

choice = raw_input('> ')

if choice == '1':
    __builtin__._ = lambda x : x
elif choice == '2':
    __builtin__._ = gettext.GNUTranslations(open("languages/spanish.mo", "rb")).ugettext # ugettext for unicode

# "game launcher" logic here
print 'Choose a game:'
print '1. DrawCardDemo'
print '2. ESR'
print '3. Go Fish'
print '4. Old Maid'
print '5. 24'
print '6. UNO'

choice = raw_input('> ')

if choice == '1':
    from DrawCardDemo import DrawDemo
    DrawDemo()
elif choice == '2':
    from ERSTableObjects import ERSTable
    ERSTable().play_game()
elif choice == '3':
    from GoFishGUI import GoFishGUI
    GoFishGUI()
elif choice == '4':
    from OldMaidTableObjects import OldMaidTable
    OldMaidTable().play_game()
elif choice == '5':
    from TwentyFourTableObjects import TwentyFourTable
    TwentyFourTable().play_game()
elif choice == '6':
    from UnoTableObjects import UnoTable
    UnoTable().play_game()
