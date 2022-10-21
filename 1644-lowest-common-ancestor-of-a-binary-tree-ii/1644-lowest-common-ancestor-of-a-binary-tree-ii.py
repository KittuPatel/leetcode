# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_found = False
        q_found = False
        
        def dfs(root):
            nonlocal p_found
            nonlocal q_found
            
            if not root:
                return None
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if root == p or root == q:
                if root == p:
                    p_found = True
                else:
                    q_found = True
                
                return root
            
            if l and r:
                return root
            else:
                return l or r            
        
        res = dfs(root)
        
        return res if p_found and q_found else None
        