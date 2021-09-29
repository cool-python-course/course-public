import unittest

from array_splitter import split


class TestArraySplitter(unittest.TestCase):

    def test_split_should_return_empty_set_if_there_is_no_valid_splitting(self):
        # given
        array = ['a', 'b', 'c']
        GROUP_COUNT_TOO_MANY = len(array) + 1
        expected = {}
        # when
        actual = split(array, GROUP_COUNT_TOO_MANY)
        # then
        self.assertEqual(actual, expected)

    def test_split_should_split_array_into_two_parts(self):
        # given
        array = ['a', 'a', 'b', 'b']
        group_count = 2
        expected = {[['a', 'a'], ['b', 'b']]}
        # when
        actual = split(array, group_count)
        # then
        self.assertEqual(actual, expected)