# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        
        newNode = TreeNode(v1+v2)
        
        newNode.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        newNode.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return newNode
        
        
#         if root1 is None and root2 is None:
#             return
        
#         if not root1:
#             return root2
        
#         elif not root2:
#             return root1
        
#         else:
#             res = root1.val + root2.val
#             newNode = TreeNode(res)
            
#             newNode.left = self.mergeTrees(root1.left, root2.left)
#             newNode.right = self.mergeTrees(root1.right, root2.right)
            
        
#         return newNode
        