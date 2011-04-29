import unittest

from CardTests import *
from DeckTests import *
from DiscardPileTests import *
from PlayerTests import *
from TableTests import *
from GoFishTests import *
from GoFishPlayerTests import *
from GoFishHumanPlayerTests import *
from GoFishAIPlayerTests import *

from GoFishPlayerTests import *
from GoFishTableTests import *

from SlapJackPlayerTests import *
from SlapJackTableTests import *

#from TwentyFourTests import *

load = unittest.TestLoader().loadTestsFromTestCase

<<<<<<< HEAD
suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable, TestGoFish, TestGoFishPlayer, TestGoFishHumanPlayer, TestGoFishAIPlayer])
=======
suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable, TestGoFishPlayer, TestGoFishTable])
>>>>>>> 1d4f7e223504fcf507b5930c85bf019ac183089e

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
