# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, curSum):
            if root is None:
                return
            
            curSum += root.val
            
            if root.left is None and root.right is None:
                return curSum == targetSum
            
            left = dfs(root.left, curSum)
            right = dfs(root.right, curSum)
            
            return left or right
            
        return dfs(root, 0)
    
        
        
        