import unittest
from CardTests import *
from DeckTests import *
from DiscardPileTests import *
from PlayerTests import *
from TableTests import *

load = unittest.TestLoader().loadTestsFromTestCase

suites = map(load, [TestCard, TestDeck, TestDiscardPile, TestPlayer, TestTable])

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
