# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.maxD = 0
        def dfs(root, depth):
            
            if root is None:
                return 0
                
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
            
            return 1 + max(left, right)
        
        return dfs(root, 1)

        