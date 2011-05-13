import unittest

from CardTests import *
from DeckTests import *
from DiscardPileTests import *
from PlayerTests import *
from TableTests import *

from GoFishTableTests import *
from GoFishPlayerTests import *
from GoFishHumanPlayerTests import *
from GoFishAIPlayerTests import *
from GoFishPlayerTests import *
from GoFishTableTests import *
#from TwentyFourTests import *

load = unittest.TestLoader().loadTestsFromTestCase

suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable, TestGoFishTable, TestGoFishPlayer, TestGoFishHumanPlayer, TestGoFishAIPlayer])

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
