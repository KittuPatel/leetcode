# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        
        if not root and subRoot:
            return False
        
        if root and not subRoot:
            return True
        
        if self.isSameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right
    
    def isSameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        
        if not tree1 or not tree2:
            return False
        
        if tree1.val != tree2.val:
            return False
        
        left = self.isSameTree(tree1.left, tree2.left)
        right = self.isSameTree(tree1.right, tree2.right)
        
        return left and right