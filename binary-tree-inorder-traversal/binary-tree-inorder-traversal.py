# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     Recursive
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.dfs(root, res)
#         return res
    
#     def dfs(self, root, res):
#         if root:
#             self.dfs(root.left, res)
#             res.append(root.val)
#             self.dfs(root.right, res)
        
    # Iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
            
            
            
            
            
            