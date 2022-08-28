# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         find middle element
        slow, fast = head, head
    
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
#         slow is the first element of second half
        
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        left, right = head, prev
        
#         reversed list right points to null
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        