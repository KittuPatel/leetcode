# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, root, minValue, maxValue):
        if not root:
            return True
        
        if not (minValue < root.val < maxValue):
            return False
        
        leftSubtree = self.helper(root.left, minValue, root.val)
        rightSubtree = self.helper(root.right, root.val, maxValue)
        
        return leftSubtree and rightSubtree