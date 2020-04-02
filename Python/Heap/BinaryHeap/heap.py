
class Heap(object):

    def __init__(self, items = None):
        if items is None:
            self.items = [0]
        else:
            self.__heapify(items)

    def size(self):
        return len(self.items) - 1

    def isempty(self):
        return self.size() == 0

    def insert(self, item):
        self.items.append(item)
        self.__bubbleup()

    def pop(self):
        if self.size() > 0:
            item = self.items[1]
            self.items[1] = self.items[self.size()]
            self.items.pop()
            self.__bubbledown(1)
            return item

    def peek(self):
        if self.size() > 0:
            return self.items[1]

    def __heapify(self, items):
        self.items = [0] + items[:]
        count = len(items)
        i = count // 2
        while i > 0:
            self.__bubbledown(i)
            i -= 1

    def __bubbleup(self):
        i = len(self.items) - 1
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i], self.items[i // 2] = self.items[i // 2], self.items[i]
            i //= 2

    def __bubbledown(self, i):
        while i * 2 <= self.size():
            minChild = self.__minchild(i)
            if self.items[minChild] < self.items[i]:
                self.items[i], self.items[minChild] = self.items[minChild], self.items[i]
            i = minChild

    def __minchild(self, i):
        if 2*i + 1 > self.size():
            return 2*i
        else:
            if (self.items[2*i] < self.items[2*i + 1]):
                return 2*i
            else:
                return 2*i + 1
