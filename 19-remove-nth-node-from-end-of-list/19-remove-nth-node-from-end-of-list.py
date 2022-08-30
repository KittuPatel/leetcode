# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         two pointer and dummy node  
#         LL -  1 -> 2 -> 3 -> None
        start = ListNode()
        start.next = head
#         LL - Dummy -> 1 -> 2 -> 3 -> None
        slow = fast = start
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start.next