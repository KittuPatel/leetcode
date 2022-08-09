# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        countHeadA = self.countNodes(headA)
        countHeadB = self.countNodes(headB)
        
        if countHeadA > countHeadB:
            d = countHeadA - countHeadB
            return self._getIntersectionNode(d, headA, headB)
        else:
            d = countHeadB - countHeadA
            return self._getIntersectionNode(d, headB, headA)
             
    
    def countNodes(self, head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def _getIntersectionNode(self, d, headA, headB):
        
        for i in range(d):
            headA = headA.next
            
        while headA is not None and headB is not None:
            if headA ==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
        
        