from .context import c_creator

import unittest

class BasicTestSuite(unittest.TestCase):


    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()