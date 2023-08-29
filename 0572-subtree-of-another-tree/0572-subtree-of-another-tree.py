# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                l= check(p.left, q.left)
                r =check(p.right, q.right)
                return l and r
            else:
                return False
        
        
        def isSub(root, subRoot):
        
            if not subRoot:
                return True
            
            if not root:
                return False
            
            if check(root, subRoot):
                return True
            
            l = isSub(root.left, subRoot)
            r = isSub(root.right, subRoot)
            return l or r
            
        
        return isSub(root, subRoot)
