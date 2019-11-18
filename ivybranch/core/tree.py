"""
Tree Algorithms for ordering and traversal.
"""
import operator

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child
    
    def get_data(self):
        return self.data
    
    def insert_left(self, data):
        if self.left_child == None:
            self.left_child = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.left_child = self.left_child
            self.left_child = t
        return None
    
    def insert_right(self, data):
        if self.right_child == None:
            self.right_child = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.right_child = self.right_child
            self.right_child = t
        return None
