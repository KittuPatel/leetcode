# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        res = 0
        
        def dfs(root):
            nonlocal res
            
            if root is None: return 0, 0
            
            left_sum, left_nodes = dfs(root.left)
            right_sum, right_nodes = dfs(root.right)
            
            s = root.val + left_sum + right_sum
            c = 1 + left_nodes + right_nodes
            
            if s // c == root.val:
                res += 1
            
            return s, c
         
        dfs(root)
        return res        
            
        
        
        
        