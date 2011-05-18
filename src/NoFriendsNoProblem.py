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
print '1. ERS'
print '2. Go Fish'
print '3. Old Maid'
print '4. 24'
print '5. UNO'

choice = raw_input('> ')

if choice == '1':
    from ERSTableObjects import ERSTable
    ERSTable().play_game()
elif choice == '2':
    from GoFishGUI import GoFishGUI
    GoFishGUI()
elif choice == '3':
    from OldMaidTableObjects import OldMaidTable
    OldMaidTable().play_game()
elif choice == '4':
    from TwentyFourTableObjects import TwentyFourTable
    TwentyFourTable().play_game()
elif choice == '5':
    from UnoTableObjects import UnoTable
    UnoTable().play_game()
