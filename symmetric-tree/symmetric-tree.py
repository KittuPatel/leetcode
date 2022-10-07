# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, leftRoot, rightRoot):
        if leftRoot and rightRoot:
            return (leftRoot.val == rightRoot.val) and self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)
        
        return leftRoot == rightRoot
    
    