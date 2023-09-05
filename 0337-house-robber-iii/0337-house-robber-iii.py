# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]  # [Maximum if not robbed, Maximum if robbed]
            
            # Recursively calculate the maximum values for left and right subtrees.
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Calculate the maximum value if the current house (node) is not robbed.
            not_robbed = max(left) + max(right)
            
            # Calculate the maximum value if the current house (node) is robbed.
            robbed = node.val + left[0] + right[0]
            
            return [not_robbed, robbed]
        
        max_values = dfs(root)
        
        # Return the maximum of the two cases: robbed and not robbed.
        return max(max_values)