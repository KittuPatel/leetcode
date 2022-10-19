class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.count = 1
        
class AllOne:
    def __init__(self):
        # Create dummy nodes to faciliate code.
        self.head, self.tail = Node("h"), Node("t")
        self.head.count = float("inf")
        self.tail.count = float("-inf")
        self.tail.left = self.head
        self.head.right = self.tail
        self.words = {}

    def inc(self, key: str) -> None:
        if key not in self.words:
            # If word hasn't appeared yet, attach it to the tail.
            new_node = Node(key, self.tail.left, self.tail)
            self.tail.left.right = self.tail.left = self.words[key] = new_node
        else:
            # If word exists, find it and move the node towards the head as long as the occurance > it's left neighbor.
            node = self.words[key]
            node.count += 1
            while node.count > node.left.count:
                self.swap(node.left, node)

    def dec(self, key: str) -> None:
        node = self.words[key]
        node.count -= 1
        if node.count == 0:
            # If count reaaches 0, we remove the node and it's mapped entry
            node.left.right = node.right
            node.right.left = node.left
            del self.words[key]
        else:
            # Move node towards the tailend
            while node.count < node.right.count:
                self.swap(node, node.right)

    def getMaxKey(self) -> str:
        # The first node of the linked list will always be the Max
        if not self.words:
            return ""
        return self.head.right.val
        
    def getMinKey(self) -> str:
        # The last node of the linkedlist will always be the Min
        if not self.words:
            return ""
        return self.tail.left.val
        
    def swap(self, n1, n2):
        n1.left.right = n2
        n2.right.left = n1
        
        n2.left = n1.left
        n1.left = n2
        n1.right = n2.right
        n2.right = n1