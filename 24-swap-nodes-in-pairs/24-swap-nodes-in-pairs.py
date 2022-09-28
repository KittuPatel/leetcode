# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev = dummy
        curr = head
        
        while curr and curr.next:
            # save few pointers
            nxtPair = curr.next.next
            secondNode = curr.next
            
            # reverse nodes        
            secondNode.next = curr
            curr.next = nxtPair
            prev.next = secondNode
            
            # update pointers
            prev = curr
            curr = nxtPair

        return dummy.next
        