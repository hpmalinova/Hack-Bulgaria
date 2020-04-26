import unittest
from deep_find_all import deep_find_all_bfs, deep_find_all_dfs


class TestDeepFindAllBFS(unittest.TestCase):
    def test_deep_find_all_bfs_when_no_keys_found_then_return_false(self):
        data = {1: 'first', 2: 'second'}
        key = 4

        self.assertFalse(deep_find_all_bfs(data, key))

    def test_deep_find_all_bfs_when_only_one_key_is_found_on_first_level(self):
        data = {1: 'first', 2: 'second', 3: 'third'}
        key = 3

        self.assertEqual(deep_find_all_bfs(data, key), ['third'])

    def test_deep_find_all_bfs_when_only_one_key_is_found_on_second_level(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}}
        key = 4

        self.assertEqual(deep_find_all_bfs(data, key), ['third'])

    def test_deep_find_all_bfs_when_only_one_key_is_found_on_deeper_level(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}, 5: {6: {7: 'fourth'}}}
        key = 7

        self.assertEqual(deep_find_all_bfs(data, key), ['fourth'])

    def test_deep_find_all_bfs_when_found_more_keys_then_return_them_all(self):
        data = {1: 'first', 2: 'second', 3: {4: {2: 'third'}}}
        key = 2

        data2 = {1: {2: {3: 'second'}}, 3: 'first'}
        key2 = 3

        data3 = {1: {4: {5: 'third'}}, 2: {6: 'first', 5: 'second'}}
        key3 = 5

        data4 = {1: 'first', 2: {1: 'second', 4: {1: 'fourth'}}, 3: {1: 'third'}}
        key4 = 1

        self.assertEqual(deep_find_all_bfs(data, key), ['second', 'third'])
        self.assertEqual(deep_find_all_bfs(data2, key2), ['first', 'second'])
        self.assertEqual(deep_find_all_bfs(data3, key3), ['second', 'third'])
        self.assertEqual(deep_find_all_bfs(data4, key4), ['first', 'second', 'third', 'fourth'])

    def test_deep_find_all_bfs_when_value_is_list(self):
        data = {1: [{2: 'second'}, {3: {4: 'third'}}], 2: 'first'}
        key = 2

        self.assertEqual(deep_find_all_bfs(data, key), ['first', 'second'])

    def test_deep_find_all_bfs_when_value_is_tuple(self):
        data = {1: ({2: 'second'}, {3: {4: 'third'}}), 2: 'first'}
        key = 2

        self.assertEqual(deep_find_all_bfs(data, key), ['first', 'second'])


class TestDeepFindAllDFS(unittest.TestCase):
    def test_deep_find_all_dfs_when_no_keys_found_then_return_false(self):
        data = {1: 'first', 2: 'second'}
        key = 4

        self.assertFalse(deep_find_all_dfs(data, key))

    def test_deep_find_all_dfs_when_only_one_key_is_found_on_first_level(self):
        data = {1: 'first', 2: 'second', 3: 'third'}
        key = 3

        self.assertEqual(deep_find_all_dfs(data, key), ['third'])

    def test_deep_find_all_dfs_when_only_one_key_is_found_on_second_level(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}}
        key = 4

        self.assertEqual(deep_find_all_dfs(data, key), ['third'])

    def test_deep_find_all_dfs_when_only_one_key_is_found_on_deeper_level(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}, 5: {6: {7: 'fourth'}}}
        key = 7

        self.assertEqual(deep_find_all_dfs(data, key), ['fourth'])

    def test_deep_find_all_dfs_when_found_more_keys_then_return_them_all(self):
        data = {1: 'first', 2: 'second', 3: {4: {2: 'third'}}}
        key = 2

        data2 = {1: {2: {3: 'first'}}, 3: 'second'}
        key2 = 3

        data3 = {1: {4: {5: 'first'}}, 2: {6: 'second', 5: 'third'}}
        key3 = 5

        data4 = {1: 'first', 2: {1: 'second', 4: {1: 'third'}}, 3: {1: 'fourth'}}
        key4 = 1

        self.assertEqual(deep_find_all_dfs(data, key), ['second', 'third'])
        self.assertEqual(deep_find_all_dfs(data2, key2), ['first', 'second'])
        self.assertEqual(deep_find_all_dfs(data3, key3), ['first', 'third'])
        self.assertEqual(deep_find_all_dfs(data4, key4), ['first', 'second', 'third', 'fourth'])

    def test_deep_find_all_dfs_when_value_is_list(self):
        data = {1: [{2: 'first'}, {3: {2: 'second'}}], 2: 'third'}
        key = 2

        self.assertEqual(deep_find_all_dfs(data, key), ['first', 'second', 'third'])

    def test_deep_find_all_dfs_when_value_is_tuple(self):
        data = {1: ({2: 'first'}, {2: {2: 'third'}}), 2: 'fourth'}
        key = 2

        self.assertEqual(deep_find_all_dfs(data, key), ['first', {2: 'third'}, 'third', 'fourth'])


if __name__ == '__main__':
    unittest.main()
