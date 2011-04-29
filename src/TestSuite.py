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

load = unittest.TestLoader().loadTestsFromTestCase

suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable, TestGoFish, TestGoFishPlayer, TestGoFishHumanPlayer, TestGoFishAIPlayer])

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
