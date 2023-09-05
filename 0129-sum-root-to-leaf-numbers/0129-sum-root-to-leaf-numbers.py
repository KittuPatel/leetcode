# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(cur, curSum):
            nonlocal total
            
            if not cur:
                return 0
            
            curSum += str(cur.val)
            if not cur.left and not cur.right:
                total += int(curSum)
                return
            
            dfs(cur.left, curSum)
            dfs(cur.right, curSum)
            
        dfs(root, '')
        return total