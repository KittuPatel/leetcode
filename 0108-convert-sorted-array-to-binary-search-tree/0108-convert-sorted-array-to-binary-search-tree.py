# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        root = None
        
        def bs(nums):
            if len(nums) == 0:
                return None
            
            l = 0
            r = len(nums)-1
            
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = bs(nums[:mid])
            root.right = bs(nums[mid+1:])
            
            return root
        
        return bs(nums)
            
            