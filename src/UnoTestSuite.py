import unittest

from UnoAIPlayerTests import *
from UnoCardTests import *
from UnoDeckTests import *
from UnoHumanPlayerTests import *
from UnoPlayerTests import *
from UnoTableTests import *

load = unittest.TestLoader().loadTestsFromTestCase

suites = map(load, [TestUnoAIPlayer, TestUnoCard, TestUnoDeck, TestUnoHumanPlayer, TestUnoPlayer, TestUnoTable])

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=1).run(alltests)
