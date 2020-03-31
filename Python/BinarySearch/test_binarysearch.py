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
        self.assertEqual(find_bitonic_peak([1, 2, 3]),          None)
        self.assertEqual(find_bitonic_peak([3, 2, 1]),          None)
        self.assertEqual(find_bitonic_peak([4, 3, 2, 1]),       None)
        self.assertEqual(find_bitonic_peak([1, 2, 3, 4]),       None)
        self.assertEqual(find_bitonic_peak([1, 3, 2]),             3)
        self.assertEqual(find_bitonic_peak([1, 3, 2, 1]),          3)
        self.assertEqual(find_bitonic_peak([1, 2, 3, 1]),          3)
        self.assertEqual(find_bitonic_peak([1, 2, 3, 4, 1]),       4)
        self.assertEqual(find_bitonic_peak([1, 6, 5, 4, 3, 2, 1]), 6)
