# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle using floyd tortoise and hare method
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #  reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # merge two halfs - second list head is at prev position
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
            
        
            