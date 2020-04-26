import unittest
from deep_update import deep_update_dfs


class TestDeepUpdateDFS(unittest.TestCase):
    def test_deep_update_dfs_when_only_one_key_is_found_then_update_it(self):
        data = {1: 'first', 2: 'second', 3: 'fourth'}
        key = 3
        new_value = 'third'
        expected_result = {1: 'first', 2: 'second', 3: 'third'}

        self.assertEqual(deep_update_dfs(data, key, new_value), expected_result)

    def test_deep_update_dfs_when_more_keys_are_found_then_update_them(self):
        data = {1: 'a', 2: {1: [{1: 'c'}]}}
        key = 1
        new_value = 'sun'
        expected_result = {1: 'sun', 2: {1: 'sun'}}

        self.assertEqual(deep_update_dfs(data, key, new_value), expected_result)


if __name__ == '__main__':
    unittest.main()
