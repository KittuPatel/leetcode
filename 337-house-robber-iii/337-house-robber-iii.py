# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # dfs returns [withRoot, withoutRoot]
        def dfs(root):
            if root is None:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # involve the current node and pick withoutRoot from children nodes
            withRoot = root.val + left[1] + right[1]
            
            # dont involve current node but pick max of left and right childs
            withoutRoot = max(left) + max(right)
            
            return [withRoot, withoutRoot]
        
        return max(dfs(root))