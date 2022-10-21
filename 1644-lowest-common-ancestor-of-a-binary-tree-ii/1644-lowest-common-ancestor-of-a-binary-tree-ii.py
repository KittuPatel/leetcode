# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.p_found = False
        self.q_found = False
        
        ans = self.dfs(root, p, q)
        
        return ans if self.p_found and self.q_found else None
        
    def dfs(self, root, p, q):

        if not root:
            return None

        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p, q)

        if root == p or root == q:
            if root == p:
                self.p_found = True
            else:
                self.q_found = True

            return root

        if l and r:
            return root
        else:
            return l or r
            