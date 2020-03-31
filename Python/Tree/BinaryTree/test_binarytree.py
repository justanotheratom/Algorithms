from unittest import TestCase
from .binarytree import BinaryTree
from .binarytree import Node

class TestBinaryTree(TestCase):

    def setUp(self) -> None:
        self.bt = BinaryTree(1)
        self.bt.root.left = Node(2)
        self.bt.root.right = Node(3)
        self.bt.root.left.left = Node(4)
        self.bt.root.left.right = Node(5)
        self.bt.root.right.left = Node(6)
        self.bt.root.right.right = Node(7)

    def test_preorder(self):
        self.assertEqual(self.bt.print_tree('preorder'), [1, 2, 4, 5, 3, 6, 7])

    def test_postorder(self):
        self.assertEqual(self.bt.print_tree('postorder'), [4, 5, 2, 6, 7, 3, 1])

    def test_inorder(self):
        self.assertEqual(self.bt.print_tree('inorder'), [4, 2, 5, 1, 6, 3, 7])

    def test_levelorder(self):
        self.assertEqual(self.bt.print_tree('levelorder'), [1, 2, 3, 4, 5, 6, 7])

    def test_reverselevelorder(self):
        self.assertEqual(self.bt.print_tree('reverselevelorder'), [4, 5, 6, 7, 2, 3, 1])

    def test_height(self):
        self.assertEqual(self.bt.height(), 2)

    def test_size(self):
        self.assertEqual(self.bt.size(), 7)