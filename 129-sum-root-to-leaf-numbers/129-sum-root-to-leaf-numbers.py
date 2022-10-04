# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, res):
            if root is None:
                return 0

            res = (res *10) + root.val
            
            if not root.left and not root.right:
                return res
            

            left = dfs(root.left, res)
            right = dfs(root.right, res)
        
            return left + right
        
        return dfs(root, 0)
        
        
        