import unittest
from deep_compare import deep_compare_dfs


class TestDeepCompareDFS(unittest.TestCase):
    # Test Non Nested input
    def test_deep_compare_dfs_when_two_lists_are_equal_then_return_true(self):
        data1 = ['first', 'second', 'third']
        data2 = ['first', 'second', 'third']

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_lists_are_not_equal_then_return_false(self):
        data1 = ['first', 'second', 'third']
        data2 = ['first', 'second', 'fourth']

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_strings_are_equal_then_return_true(self):
        data1 = 'first'
        data2 = 'first'

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_strings_are_not_equal_then_return_false(self):
        data1 = 'first'
        data2 = 'fourth'

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_tuples_are_equal_then_return_true(self):
        data1 = ('first', 'second', 'third')
        data2 = ('first', 'second', 'third')

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_tuples_are_not_equal_then_return_false(self):
        data1 = ('first', 'second', 'third')
        data2 = ('first', 'second', 'fourth')

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_dictionaries_are_equal_then_return_true(self):
        data1 = {1: 'first', 2: 'second'}
        data2 = {1: 'first', 2: 'second'}

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_dictionaries_are_not_equal_then_return_false(self):
        data1 = {1: 'first', 2: 'second'}
        data2 = {1: 'first', 2: 'third'}

        self.assertFalse(deep_compare_dfs(data1, data2))

    # Test Nested input
    def test_deep_compare_dfs_when_two_objects_are_equal1(self):
        data1 = [{1: 'first', 2: 'second'}, 5, 'abc']
        data2 = [{1: 'first', 2: 'second'}, 5, 'abc']

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_objects_are_not_equal1(self):
        data1 = [{1: 'first', 2: 'sec'}, 5, 'abc']
        data2 = [{1: 'first', 2: 'second'}, 5, 'abc']

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_objects_are_equal2(self):
        data1 = [{5: [{1: 'first', 2: 'second'}]}]
        data2 = [{5: [{1: 'first', 2: 'second'}]}]

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_objects_are_not_equal2(self):
        data1 = [{5: [{1: 'first', 2: 'sec'}]}]
        data2 = [{5: [{1: 'first', 2: 'second'}]}]

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_objects_are_equal3(self):
        data1 = {5: [{1: 'first', 2: 'second'}], 3: 'asdsa'}
        data2 = {3: 'asdsa', 5: [{1: 'first', 2: 'second'}]}

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_objects_are_not_equal3(self):
        data1 = {5: [{1: 'first', 3: 'second'}], 3: 'asdsa'}
        data2 = {3: 'asdsa', 5: [{1: 'first', 2: 'second'}]}

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_two_nested_dictionaries_are_equal_then_return_true(self):
        data1 = {5: {1: 'first', 2: 'second'}}
        data2 = {5: {1: 'first', 2: 'second'}}

        self.assertTrue(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_nested_dictionaries_have_different_keys_then_return_false(self):
        data1 = {5: {1: 'first', 2: 'second'}}
        data2 = {5: {1: 'first', 3: 'second'}}

        self.assertFalse(deep_compare_dfs(data1, data2))

    def test_deep_compare_dfs_when_nested_dictionaries_have_different_values_then_return_false(self):
        data1 = {5: {1: 'first', 2: 'second'}}
        data2 = {5: {1: 'first', 2: 'sec'}}

        self.assertFalse(deep_compare_dfs(data1, data2))


if __name__ == '__main__':
    unittest.main()
