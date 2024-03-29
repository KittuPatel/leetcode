# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, curSum):
            if not root:
                return False
            
            curSum += root.val
            if not root.left and not root.right:
                return targetSum == curSum
            return helper(root.left, curSum) or helper(root.right, curSum)
        
        return helper(root, 0)