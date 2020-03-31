from .queue import Queue
from .stack import Stack

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def is_leaf(self):
        return (self.left is None) and (self.right is None)

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        result = []
        if traversal_type == 'preorder':
            result = self.print_preorder(self.root, result)
        elif traversal_type == 'postorder':
            result = self.print_postorder(self.root, result)
        elif traversal_type == 'inorder':
            result = self.print_inorder(self.root, result)
        elif traversal_type == 'levelorder':
            result = self.print_levelorder(self.root, result)
        elif traversal_type == 'reverselevelorder':
            result = self.print_reverselevelorder(self.root, result)
        return result

    def print_preorder(self, startnode, result):
        if startnode:
            result.append(startnode.value)
            result = self.print_preorder(startnode.left, result)
            result = self.print_preorder(startnode.right, result)
        return result

    def print_postorder(self, startnode, result):
        if startnode:
            result = self.print_postorder(startnode.left, result)
            result = self.print_postorder(startnode.right, result)
            result.append(startnode.value)
        return result

    def print_inorder(self, startnode, result):
        if startnode:
            result = self.print_inorder(startnode.left, result)
            result.append(startnode.value)
            result = self.print_inorder(startnode.right, result)
        return result

    def print_levelorder(self, startnode, result):
        q = Queue()
        q.push(startnode)
        while not q.is_empty():
            n = q.pop()
            result.append(n.value)
            if n.left:
                q.push(n.left)
            if n.right:
                q.push(n.right)
        return result

    def print_reverselevelorder(self, startnode, result):
        q = Queue()
        s = Stack()
        q.push(startnode)
        while not q.is_empty():
            n = q.pop()
            s.push(n.value)
            if n.right:
                q.push(n.right)
            if n.left:
                q.push(n.left)
        while not s.is_empty():
            result.append(s.pop())
        return result

    def height(self):

        def height_recursive(node):
            if node.is_leaf():
                return 0
            return 1 + max(height_recursive(node.left), height_recursive(node.right))

        return height_recursive(self.root)

    def size(self):

        def size_recursive(node):
            if node is None:
                return 0
            return 1 + size_recursive(node.left) + size_recursive(node.right)

        return size_recursive(self.root)
