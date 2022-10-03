# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, None, 0, len(nums)-1)
    
    def helper(self, array, bst, start, stop):
        if start > stop:
            return
        
        mid = (start + stop) // 2
        node = TreeNode(array[mid])
        if bst is None:
            bst = node
        else:
            # insert node
            if array[mid] < bst.val:
                bst.left = node
                bst = bst.left
            else:
                bst.right = node
                bst = bst.right
        
        
        self.helper(array, bst, start, mid - 1)
        self.helper(array, bst, mid + 1, stop)
        
        return bst