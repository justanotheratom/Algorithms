from unittest import TestCase
from .heap import Heap

class TestHeap(TestCase):

    def test_insert(self):
        test_heap = Heap()
        test_heap.insert(3)
        test_heap.insert(2)
        test_heap.insert(1)
        self.assertEqual(test_heap.size(), 3)
        self.assertEqual(test_heap.peek(), 1)
        self.assertEqual(test_heap.pop(), 1)
        self.assertEqual(test_heap.peek(), 2)
        self.assertEqual(test_heap.pop(), 2)
        self.assertEqual(test_heap.peek(), 3)
        self.assertEqual(test_heap.pop(), 3)
        self.assertEqual(test_heap.size(), 0)

