import unittest
from tests_12_3 import RunnerTest
from tests_12_3 import TournamentTest


class AllTests(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
        self.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))
