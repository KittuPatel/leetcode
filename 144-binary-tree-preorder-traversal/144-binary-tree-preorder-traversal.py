# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.dfs(root, res)
#         return res
    
#     def dfs(self, root, res):
#         if root:
#             res.append(root.val)
#             self.dfs(root.left, res)
#             self.dfs(root.right, res)
    
    # Iterative solution
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
    