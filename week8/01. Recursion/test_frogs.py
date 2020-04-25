import unittest
from frogs import *


class TestFrogs(unittest.TestCase):
    def setUp(self):
        self.lake = ['>', '>', '>', '_', '<', '<', '<']

    def test_init_lake(self):
        self.assertEqual(init_lake(3), self.lake)

    def test_final_lake(self):
        expected_result = ['<', '<', '<', '_', '>', '>', '>']

        self.assertEqual(final_lake(3), expected_result)

    def test_move_left_frog_with_one_step(self):
        expected_result = ['>', '>', '_', '>', '<', '<', '<']

        self.assertEqual(move_frog(2, self.lake), expected_result)

    def test_move_right_frog_with_one_step(self):
        expected_result = ['>', '>', '>', '<', '_', '<', '<']

        self.assertEqual(move_frog(4, self.lake), expected_result)

    def test_move_left_frog_with_two_steps(self):
        expected_result = ['>', '>', '_', '<', '>', '<', '<']
        move_frog(4, self.lake)

        self.assertEqual(move_frog(2, self.lake), expected_result)

    def test_move_right_frog_with_two_steps(self):
        expected_result = ['>', '>', '<', '>', '_', '<', '<']
        move_frog(2, self.lake)

        self.assertEqual(move_frog(4, self.lake), expected_result)

    def test_move_frog_when_not_possible_move_then_return_false(self):
        self.assertFalse(move_frog(0, self.lake))

    def test_move_frog_when_try_to_move_rock_then_return_false(self):
        self.assertFalse(move_frog(3, self.lake))

    def test_all_moves_when(self):
        expected_result = [['>', '_', '>', '>', '<', '<', '<'],
                           ['>', '>', '_', '>', '<', '<', '<'],
                           ['>', '>', '>', '<', '_', '<', '<'],
                           ['>', '>', '>', '<', '<', '_', '<']]

        self.assertEqual(all_moves_for_turn(self.lake), expected_result)
        self.assertEqual(['>', '>', '>', '_', '<', '<', '<'], self.lake)

    def test_all_moves_does_not_change_original_lake(self):
        all_moves_for_turn(self.lake)

        self.assertEqual(['>', '>', '>', '_', '<', '<', '<'], self.lake)

    def test_dfs(self):
        lake = ['>', '>', '>', '_', '<', '<', '<']
        final_lake = ['<', '<', '<', '_', '>', '>', '>']
        expected_result = [['>', '>', '>', '_', '<', '<', '<'],
                           ['>', '>', '_', '>', '<', '<', '<'],
                           ['>', '>', '<', '>', '_', '<', '<'],
                           ['>', '>', '<', '>', '<', '_', '<'],
                           ['>', '>', '<', '_', '<', '>', '<'],
                           ['>', '_', '<', '>', '<', '>', '<'],
                           ['_', '>', '<', '>', '<', '>', '<'],
                           ['<', '>', '_', '>', '<', '>', '<'],
                           ['<', '>', '<', '>', '_', '>', '<'],
                           ['<', '>', '<', '>', '<', '>', '_'],
                           ['<', '>', '<', '>', '<', '_', '>'],
                           ['<', '>', '<', '_', '<', '>', '>'],
                           ['<', '_', '<', '>', '<', '>', '>'],
                           ['<', '<', '_', '>', '<', '>', '>'],
                           ['<', '<', '<', '>', '_', '>', '>'],
                           ['<', '<', '<', '_', '>', '>', '>']]

        self.assertEqual(dfs(lake, final_lake), expected_result)


if __name__ == '__main__':
    unittest.main()
