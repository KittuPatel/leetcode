# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # pre order traversal or post order traversal both works!!   
        if root is None:
            return
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        self.swapNodes(root)
        
        return root
        
    def swapNodes(self, node):
        node.left, node.right = node.right, node.left