class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # map key to nodes   
        self.cache = {} 
        
        # left = Least Recently Used, right = Most Recently Used
        self.left, self.right = Node(0, 0), Node(0, 0)
        # connect these left and right pointers
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    
    
    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    
    # insert node at right i.e, (Most recently used)
    def insert(self, node):
        prevNode = self.right.prev
        nextNode = self.right
        prevNode.next = node
        nextNode.prev = node
        node.prev = prevNode
        node.next = nextNode

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        # first inserting and then checking if it exceeds capacity,
        # if it exceeds capacity, then removing the node.
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # remove from the left LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)