"""
Doubly Linked List implementation.
"""

class ListNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class LinkedList:
    """
    O(n) insert by index, O(1) append.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.previous = None
        self.size = 0
    

    def _inner_action(self, action, index, node=None):
        i = 1
        self.previous = self.head
        self.current = self.head.next
        while i < self.size:
            if (i == index) and (action == "add"):
                self.previous.next = node
                node.prev = self.previous
                self.current.prev = node
                node.next = self.current
                return None
            elif (i == index) and (action == "del"):
                self.previous.next = self.current.next
                self.current.next.prev = self.previous
                del self.current
                return None
            else:
                i = i + 1
                self.previous = self.current
                self.current = self.current.next


    def append(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size = self.size + 1
        return None


    def insert(self, node, index):
        self._inner_action("add", index, node)
        self.size = self.size + 1
        return None


    def del_node(self, index):
        if self.size != 0:
            self._inner_action("del", index)
            self.size = self.size - 1
        else:
            raise ValueError


    def __iter__(self):
        i = 0
        while i < self.size:
            if (i == 0):
                self.current = self.head
            else:
                self.current = self.current.next
            yield self.current
            i = i + 1


    def __sizeof__(self):
        return self.size
