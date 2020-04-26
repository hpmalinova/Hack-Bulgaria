import unittest
from deep_apply import *


class TestDeepUpdateDFS(unittest.TestCase):
    def test_deep_apply_dfs_on_one_level(self):
        data = {1: 'first', 2: 'second', 3: 'third'}
        expected_result = {1: 'first!', 2: 'second!', 3: 'third!'}

        self.assertEqual(deep_apply_dfs(some_func, data), expected_result)

    def test_deep_apply_dfs_on_more_levels(self):
        data = {1: 'a', 2: {3: [{4: 'c'}]}}
        expected_result = {1: 'a!', 2: {3: [{4: 'c!'}]}}

        self.assertEqual(deep_apply_dfs(some_func, data), expected_result)


if __name__ == '__main__':
    unittest.main()
