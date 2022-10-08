"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        queue = collections.deque([root])
        
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    # An important check so that we do not wire the node to the node on the next level.
                    if i < qLen-1:
                        node.next = queue[0]
                    queue.append(node.left)
                    queue.append(node.right)
                    
        return root
        