
def assume(assumption):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        else:
            self.head = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            curr = self.head
            self.head = new_node
            new_node.next = curr
            curr.prev = new_node
        else:
            self.head = new_node

    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                break
            curr = curr.next

    def delete_node(self, node):
        assume(node is not None)
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        else:
            self.head = next
        if next:
            next.prev = prev

    def add_after_node(self, key, data):
        curr = self.head
        while curr:
            if curr.data == key:
                new_node = Node(data)
                tmp = curr.next
                curr.next = new_node
                new_node.next = tmp
                new_node.prev = curr
                if tmp:
                    tmp.prev = new_node
                break
            curr = curr.next

    def add_before_node(self, key, data):
        curr = self.head
        while curr:
            if curr.data == key:
                new_node = Node(data)
                new_node.next = curr
                prev = curr.prev
                curr.prev = new_node
                if prev:
                    prev.next = new_node
                    new_node.prev = prev
                else:
                    self.head = new_node
                break
            curr = curr.next

    def reverse(self):
        curr = self.head
        next = curr.next
        while next:
            prev = curr.prev
            curr.prev = next
            curr.next = prev
            curr = next
            next = curr.next
        curr.next = curr.prev
        self.head = curr

    def remove_duplicates(self):
        curr = self.head
        seen = dict()
        while curr:
            next = curr.next
            if curr.data not in seen:
                seen[curr.data] = 1
            else:
                self.delete_node(curr)
            curr = next

    def pairs_with_sum(self, target_sum):
        result = []
        p = self.head
        while p:
            q = p.next
            while q:
                if (p.data + q.data) == target_sum:
                    result.append([p.data, q.data])
                    break
                q = q.next
            p = p.next
        return result

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, ', ', sep='', end='')
            curr = curr.next
        print()

dll = DoublyLinkedList()
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.prepend(2)
dll.prepend(3)
dll.prepend(4)
dll.add_after_node(2, 1)
dll.add_after_node(5, 6)
dll.add_before_node(4, 5)
dll.add_before_node(1, 1)
dll.delete(5)
dll.delete(5)
dll.delete(6)
dll.print_list()
dll.reverse()
dll.print_list()
dll.remove_duplicates()
dll.print_list()
print(dll.pairs_with_sum(5))
