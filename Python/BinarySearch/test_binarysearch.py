from unittest import TestCase
from .binarysearch import *

class TestBinarySearch(TestCase):

    def setUp(self) -> None:
        self.items = [i for i in range(1, 15, 2)]

    def test_binarysearch_iterative(self):
        self.assertEqual(binarysearch_iterative(self.items, 10), False)
        self.assertEqual(binarysearch_iterative(self.items, 11), True)
        self.assertEqual(binarysearch_iterative(self.items,  1), True)
        self.assertEqual(binarysearch_iterative(self.items, 13), True)

    def test_binarysearch_recursive(self):
        self.assertEqual(binarysearch_recursive(self.items, 10), False)
        self.assertEqual(binarysearch_recursive(self.items, 11), True)
        self.assertEqual(binarysearch_recursive(self.items,  1), True)
        self.assertEqual(binarysearch_recursive(self.items, 13), True)

    def test_find_closest_number(self):
        self.assertEqual(find_closest_number([], 3), None)
        self.assertEqual(find_closest_number([1000], 3), 1000)
        self.assertEqual(find_closest_number([1, 4], 3), 4)
        self.assertEqual(find_closest_number([2, 5], 3), 2)
        self.assertEqual(find_closest_number([1, 5], 3), 1)
        self.assertEqual(find_closest_number([1, 3, 4, 4, 7, 9], 11), 9)
        self.assertEqual(find_closest_number([2, 5, 6, 7, 8, 8, 9], 4), 5)
        self.assertEqual(find_closest_number([4, 6, 10], 7), 6)
        self.assertEqual(find_closest_number([4, 6, 10], 4), 4)
        self.assertEqual(find_closest_number([1, 3, 8, 10, 15], 12), 10)
        self.assertEqual(find_closest_number([4, 6, 10], 17), 10)

    def test_find_fixed_point(self):
        self.assertEqual(find_fixed_point([]), None)
        self.assertEqual(find_fixed_point([0]), 0)
        self.assertEqual(find_fixed_point([1]), None)
        self.assertEqual(find_fixed_point([-2, 0, 2, 3]), 2)
        self.assertEqual(find_fixed_point([-2, -1, 2]), 2)
        self.assertEqual(find_fixed_point([-10, -5, 0, 3, 7]), 3)
        self.assertEqual(find_fixed_point([0, 2, 5, 8, 17]), 0)
        self.assertEqual(find_fixed_point([-10, -5, 3, 4, 7, 9]), None)

    def test_find_bitonic_peak(self):
        self.assertEqual(find_bitonic_peak([]),                 None)
        self.assertEqual(find_bitonic_peak([1]),                None)
        self.assertEqual(find_bitonic_peak([1, 2]),             None)
        self.assertEqual(find_bitonic_peak([1, 3, 2]),             3)
        self.assertEqual(find_bitonic_peak([1, 3, 2, 1]),          3)
        self.assertEqual(find_bitonic_peak([1, 2, 3, 1]),          3)
        self.assertEqual(find_bitonic_peak([1, 2, 3, 4, 1]),       4)
        self.assertEqual(find_bitonic_peak([1, 6, 5, 4, 3, 2, 1]), 6)

    def test_find_ceiling(self):
        self.assertEqual(find_ceiling([], 3), None)
        self.assertEqual(find_ceiling([1], 3), None)
        self.assertEqual(find_ceiling([300], 3), 300)
        self.assertEqual(find_ceiling([4, 6, 10], 6), 6)
        self.assertEqual(find_ceiling([1, 3, 8, 10, 15], 12), 15)
        self.assertEqual(find_ceiling([4, 6, 10], 17), None)
        self.assertEqual(find_ceiling([4, 6, 10], -1), 4)

    def test_find_next_letter(self):
        self.assertEqual(find_next_letter([],         'c'), None)
        self.assertEqual(find_next_letter(['c'],      'c'), None)
        self.assertEqual(find_next_letter(['a'],      'c'), 'a')
        self.assertEqual(find_next_letter(['d'],      'c'), 'd')
        self.assertEqual(find_next_letter(['b', 'c'], 'c'), 'b')
        self.assertEqual(find_next_letter(['b', 'c'], 'a'), 'b')
        self.assertEqual(find_next_letter(['a', 'c', 'f', 'h'], 'f'), 'h')
        self.assertEqual(find_next_letter(['a', 'c', 'f', 'h'], 'b'), 'c')
        self.assertEqual(find_next_letter(['a', 'c', 'f', 'h'], 'm'), 'a')
        self.assertEqual(find_next_letter(['a', 'c', 'f', 'h'], 'h'), 'a')

    def test_find_range(self):
        self.assertEqual(find_range([],                 3), [-1, -1])
        self.assertEqual(find_range([1],                3), [-1, -1])
        self.assertEqual(find_range([3],                3), [0, 0])
        self.assertEqual(find_range([3, 3],             3), [0, 1])
        self.assertEqual(find_range([3, 3, 4],          3), [0, 1])
        self.assertEqual(find_range([1, 3, 3, 4],       3), [1, 2])
        self.assertEqual(find_range([4, 6, 6, 6, 9],    6), [1, 3])
        self.assertEqual(find_range([1, 3, 8, 10, 15], 10), [3, 3])
        self.assertEqual(find_range([1, 3, 8, 10, 15], 12), [-1, -1])

    def test_infinite_array(self):
        self.assertEqual(search_in_infinite_array(InfiniteArray([]),  3), None)
        self.assertEqual(search_in_infinite_array(InfiniteArray([1]), 3), None)
        self.assertEqual(search_in_infinite_array(InfiniteArray([3]), 3), 0)
        self.assertEqual(search_in_infinite_array(InfiniteArray([5]), 3), None)
        self.assertEqual(search_in_infinite_array(InfiniteArray([4, 6, 8, 10, 12, 14]), 12), 14)
        self.assertEqual(search_in_infinite_array(InfiniteArray([4, 6, 8, 10, 12, 14]), 11), None)
        self.assertEqual(search_in_infinite_array(InfiniteArray([1, 3, 8, 10, 15]), 15), 4)
        self.assertEqual(search_in_infinite_array(InfiniteArray([1, 3, 8, 10, 15]), 200), None)
