# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        minValue = float("inf")
        ansVal = root.val
        
        def dfs(root):
            nonlocal minValue, ansVal
            
            if not root:
                return
            
            if abs(root.val - target) < minValue:
                minValue = abs(root.val - target)
                ansVal = root.val
                
            dfs(root.left)
            dfs(root.right)
            
        
        dfs(root)
        return ansVal