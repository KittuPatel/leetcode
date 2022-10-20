# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        res = set()
        
        def dfs(root):
            if root is not None:
                res.add(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        res.remove(min(res))
        if len(res) >= 1:
            return min(res)
        else:
            return -1
            