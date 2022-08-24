class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        
        #left = LRU, right = Most recently used
        self.left = Node(0,0)
        self.right = Node(0,0)
        
        self.left.next = self.right
        self.right.prev = self.left
  
    #remove node from list (lru)
    def remove(self,node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    #insert node at right
    def insert(self,node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            #remove and delete the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
            
            
            
            
            
            
            
            
            
            
            
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)