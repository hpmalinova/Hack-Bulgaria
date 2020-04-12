import unittest

from chain import chain
from compress import compress
from cycle import cycle
from itertools import islice


class TestChain(unittest.TestCase):
    def test_when_first_iterable_is_empty(self):
        iterable1 = []
        iterable2 = list(range(4, 7))

        expected_result = list(range(4, 7))

        self.assertEqual(list(chain(iterable1, iterable2)), expected_result)

    def test_when_second_iterable_is_empty(self):
        iterable1 = list(range(4, 7))
        iterable2 = []

        expected_result = list(range(4, 7))

        self.assertEqual(list(chain(iterable1, iterable2)), expected_result)

    def test_when_both_iterables_are_empty(self):
        iterable1 = []
        iterable2 = []

        expected_result = []

        self.assertEqual(list(chain(iterable1, iterable2)), expected_result)

    def test_when_both_iterables_are_non_empty_then_return_them_consecutively(self):
        iterable1 = list(range(4, 7))
        iterable2 = list(range(1, 4))

        expected_result = [4, 5, 6, 1, 2, 3]

        self.assertEqual(list(chain(iterable1, iterable2)), expected_result)

    def test_when_iterables_are_tuples(self):
        iterable1 = (-1, 0)
        iterable2 = (1, 2)

        expected_result = tuple(range(-1, 3))

        self.assertEqual(tuple(chain(iterable1, iterable2)), expected_result)


class TestCompress(unittest.TestCase):
    def test_when_mask_contains_only_False_then_return_empty_iterable(self):
        iterable = list(range(0, 5))
        mask = [False for i in range(0, 5)]

        expected_result = []

        self.assertEqual(list(compress(iterable, mask)), expected_result)

    def test_when_mask_contains_only_True_then_return_whole_iterable(self):
        iterable = list(range(0, 5))
        mask = [True for i in range(0, 5)]

        expected_result = list(range(0, 5))

        self.assertEqual(list(compress(iterable, mask)), expected_result)

    def test_when_mask_contains_both_True_and_False_then_return_only_True_from_iterable(self):
        iterable = list(range(0, 5))
        mask = [True, False, True, False, True]

        expected_result = [0, 2, 4]

        self.assertEqual(list(compress(iterable, mask)), expected_result)

    def test_when_iterable_is_tuple(self):
        iterable = (5, 4, 5, 6, 3, 1)
        mask = (True, True, False, False, True, True)

        expected_result = (5, 4, 3, 1)

        self.assertEqual(tuple(compress(iterable, mask)), expected_result)


class TestCycle(unittest.TestCase):
    def test_cycle_with_islice(self):
        endless = cycle([1, 2, 3])
        expected_result = [1, 2, 3, 1, 2, 3]

        self.assertEqual(list(islice(endless, 6)), expected_result)


if __name__ == '__main__':
    unittest.main()
