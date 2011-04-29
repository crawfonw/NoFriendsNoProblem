import unittest

from CardTests import *
from DeckTests import *
from DiscardPileTests import *
from PlayerTests import *
from TableTests import *

from GoFishPlayerTests import *
from GoFishTableTests import *

#from SlapJackPlayerTests import *
#from SlapJackTableTests import *

from TwentyFourTests import *

load = unittest.TestLoader().loadTestsFromTestCase

suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable, TestGoFishPlayer, TestGoFishTable, TestTwentyFour])

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
