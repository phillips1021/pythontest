from unittest import TestCase
from simpletest.SimpleTest import split_amount


class TestSplitting(TestCase):
    def test_split_amount(self):
        self.assertEqual([1], split_amount(1,1))
        self.assertEqual([2, 2], split_amount(4, 2))
        self.assertEqual([2, 2, 1], split_amount(5, 3))
        self.assertEqual([3, 3, 2, 2, 2], split_amount(12, 5))

# can run from command line - in root directory pythontest
# python3 -m unittest testsimpletest/test_splitting.py