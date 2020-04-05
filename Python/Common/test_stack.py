from unittest import TestCase
from .stack import Stack

class TestStack(TestCase):

    def test_all(self):
        myStack = Stack()

        self.assertEqual(myStack.isempty(), True)
        myStack.push(1)
        self.assertEqual(myStack.isempty(), False)
        self.assertEqual(myStack.peek(), 1)
        self.assertEqual(myStack.pop(), 1)
        self.assertEqual(myStack.isempty(), True)
        myStack.push(1)
        myStack.push(2)
        self.assertEqual(myStack.peek(), 2)
        self.assertEqual(len(myStack), 2)
        self.assertEqual(myStack.pop(), 2)
        self.assertEqual(myStack.pop(), 1)
        self.assertEqual(myStack.isempty(), True)
