# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head
        
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
#         length = 0
#         cur = head
#         while cur is not None:
#             length += 1
#             cur = cur.next
        
#         length //= 2
#         length += 1
        
#         pointer = 1
#         cur = head
#         while length != pointer:
#             pointer += 1
#             cur = cur.next
        
#         return cur
        
        