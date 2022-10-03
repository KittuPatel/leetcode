# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxValue):
            
            if root is None:
                return 0
            
            res = 1 if root.val >= maxValue else 0
            maxValue = max(root.val, maxValue)
            
            res += dfs(root.left, maxValue)
            res += dfs(root.right, maxValue)         
            
            return res
            
        return dfs(root, float("-inf"))
        
            