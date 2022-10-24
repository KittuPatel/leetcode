"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        current = head
        stack = []
        
        while current or stack:
            if current.child:
                if current.next:
                    stack.append(current.next)
                    
                childNode = current.child
                current.child = None
                current.next, childNode.prev = childNode, current
                
            elif current.next is None and stack:
                nextNode = stack.pop()
                nextNode.prev, current.next = current, nextNode
                
            current = current.next    
            
        return head
#         stack = []
#         start = head
        
#         while head or stack:
#             if head.child:
#                 if head.next:
#                     stack.append(head.next)
#                     head.next = head.child
#                     head.next.prev = head
#                     head.child = None
            
#             if head.next == None and len(stack) != 0: 
#                 head.next = stack.pop()
#                 head.next.prev = head
            
#             head = head.next
        
#         return start
    
    