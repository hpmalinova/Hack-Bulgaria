import unittest
from deep_find import deep_find_bfs, deep_find_dfs


class TestDeepFindBFS(unittest.TestCase):
    def test_deep_find_bfs_when_key_is_in_the_first_level_then_return_its_value(self):
        data = {1: 'first', 2: 'second'}
        key = 1

        self.assertEqual(deep_find_bfs(data, key), 'first')

    def test_deep_find_bfs_when_key_is_not_in_any_level_then_return_false(self):
        data = {1: 'first', 2: 'second'}
        key = 6

        self.assertFalse(deep_find_bfs(data, key))

    def test_deep_find_bfs_when_key_is_one_level_deeper_then_return_its_value(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}}
        key = 4

        self.assertEqual(deep_find_bfs(data, key), 'third')

    def test_deep_find_bfs_when_key_is_in_a_deeper_level_then_return_its_value(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}, 5: {6: {7: 'fourth'}}}
        key = 7

        self.assertEqual(deep_find_bfs(data, key), 'fourth')

    def test_deep_find_bfs_when_found_two_keys_then_return_the_value_of_the_first_found(self):
        data = {1: 'first', 2: 'second', 3: {4: {2: 'third'}}}
        key = 2

        data2 = {1: {2: {3: 'first'}}, 3: 'second'}
        key2 = 3

        data3 = {1: {4: {5: 'third_level'}}, 2: {6: 'second_level', 5: 'second_level'}}
        key3 = 5

        self.assertEqual(deep_find_bfs(data, key), 'second')
        self.assertEqual(deep_find_bfs(data2, key2), 'second')
        self.assertEqual(deep_find_bfs(data3, key3), 'second_level')

    def test_deep_find_bfs_when_value_is_list(self):
        data = {1: [{2: 'first'}, {3: 'second', 4: 'third'}], 2: 'fourth'}
        key = 2

        self.assertEqual(deep_find_bfs(data, key), 'fourth')

    def test_deep_find_bfs_when_value_is_tuple(self):
        data = {1: ({2: 'first'}, {3: 'second', 4: 'third'}), 2: 'fourth'}
        key = 2

        self.assertEqual(deep_find_bfs(data, key), 'fourth')


class TestDeepFindDFS(unittest.TestCase):
    def test_deep_find_dfs_when_key_is_in_the_first_level_then_return_its_value(self):
        data = {1: 'first', 2: 'second'}
        key = 1

        self.assertEqual(deep_find_dfs(data, key), 'first')

    def test_deep_find_dfs_when_key_is_not_in_any_level_then_return_false(self):
        data = {1: 'first', 2: 'second'}
        key = 6

        self.assertFalse(deep_find_dfs(data, key))

    def test_deep_find_dfs_when_key_is_one_level_deeper_then_return_its_value(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}}
        key = 4

        self.assertEqual(deep_find_dfs(data, key), 'third')

    def test_deep_find_dfs_when_key_is_in_a_deeper_level_then_return_its_value(self):
        data = {1: 'first', 2: 'second', 3: {4: 'third'}, 5: {6: {7: 'fourth'}}}
        key = 7

        self.assertEqual(deep_find_dfs(data, key), 'fourth')

    def test_deep_find_dfs_when_found_two_keys_then_return_the_value_of_the_first_found(self):
        data = {1: 'first', 2: 'second', 3: {4: {2: 'third'}}}
        key = 2

        data2 = {1: {2: {3: 'first'}}, 3: 'second'}
        key2 = 3

        data3 = {1: {4: {5: 'third_level'}}, 2: {6: 'second_level', 5: 'second_level'}}
        key3 = 5

        self.assertEqual(deep_find_dfs(data, key), 'second')
        self.assertEqual(deep_find_dfs(data2, key2), 'first')
        self.assertEqual(deep_find_dfs(data3, key3), 'third_level')

    def test_deep_find_dfs_when_value_is_list(self):
        data = {1: [{2: 'first'}, {3: 'second', 4: 'third'}], 2: 'fourth'}
        key = 2

        self.assertEqual(deep_find_dfs(data, key), 'first')

    def test_deep_find_dfs_when_value_is_tuple(self):
        data = {1: ({2: 'first'}, {3: 'second', 4: 'third'}), 2: 'fourth'}
        key = 2

        self.assertEqual(deep_find_dfs(data, key), 'first')


if __name__ == '__main__':
    unittest.main()
