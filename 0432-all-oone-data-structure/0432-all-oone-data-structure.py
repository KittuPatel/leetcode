class Node:
    def __init__(self, val= 0):
        self.val = val
        self.next = None
        self.pre = None
        self.arr = set()


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.pre = self.tail, self.head
        self.d = {}
        
    def move_forward(self, node, key):
        if node.val+1 != node.next.val:
            newNode = Node(node.val+1)
            newNode.pre, newNode.next = node, node.next
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.next
        newNode.arr.add(key)
        return newNode
    
    def pre(self, node, key):
        if node.val-1 != node.pre.val:
            newNode = Node(node.val-1)
            newNode.pre, newNode.next = node.pre, node
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.pre
        newNode.arr.add(key)
        return newNode

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.d:
            node = self.head
        else:
            node = self.d[key]
            node.arr.discard(key)
            
        self.d[key] = self.move_forward(node, key)
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key in self.d:
            node = self.d[key]
            node.arr.discard(key)
            if node.val != 1:
                self.d[key] = self.pre(node, key)
            else:
                del self.d[key]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        node = self.tail.pre
        while node and len(node.arr) == 0:
            node = node.pre
        
        if not node:
            return ""
        
        val = node.arr.pop()
        node.arr.add(val)
        return val
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        node = self.head.next
        while node and len(node.arr) == 0:
            node = node.next
        if not node:
            return ""
        
        val = node.arr.pop()
        node.arr.add(val)
        return val