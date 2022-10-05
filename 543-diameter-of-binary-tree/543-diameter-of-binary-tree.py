# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # keep track of max depth for every node
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # diameter = 
            res[0] = max(res[0], 2 + left + right)
            
            # return height for each node
            return (1 + max(left, right))
        
        
        dfs(root)
        return res[0]

            