from heapq import *

class Heap(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        heappush(self.items, item)

    def pop(self):
        return heappop(self.items)

    def top(self):
        return self.items[0]

    def isempty(self):
        return len(self.items) == 0