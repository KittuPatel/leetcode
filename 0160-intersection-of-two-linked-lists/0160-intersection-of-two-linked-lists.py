# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        l1, l2 = headA, headB
        
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
            
        return l1 or l2
        
        
#         cur = headA
#         hashset = set()
#         while cur:
#             hashset.add(cur)
#             cur = cur.next
            
        
#         cur = headB
#         while cur:
#             if cur in hashset:
#                 return cur
#             cur = cur.next
            
#         return None
        