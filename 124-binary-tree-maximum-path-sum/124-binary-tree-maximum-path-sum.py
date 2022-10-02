# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        #  return max path without split    
        def dfs(node):
            if node is None:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # just computing max path sum with split (not returning)
            res[0] = max(res[0], node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        
        return res[0]
            