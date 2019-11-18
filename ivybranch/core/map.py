"""
Simple String Hash Map Implementation
"""

class Hashmap:
    """
    O(n) build of indices, O(1) insert/get/delete
    """
    def __init__(self):
        self.size = 9973
        self.values = [0 for i in range(0, self.size)]
        self.keys = [0 for i in range(0, self.size)]

        
    def put_item(self, key, value, delete=False):
        index = self._hash_item(key)
        if self.values[index] != 0:
            raise KeyError
        else:
            self.values[index] = value
            if delete:
                self.keys[index] = 0
            else:
                self.keys[index] = key
        return None
    
    def get_item(self, key):
        try:
            item = self.values[self._hash_item(key)]
        except:
            raise KeyError
        return item
    
    def del_item(self, key):
        self.put_item(key, 0, delete=True)
        return None

    def _hash_item(self, item):
        """
        Custom basic hash function, sum of ords
        """
        total = 0
        for i in list(item):
            total = total + ord(i)
        return total % self.size
