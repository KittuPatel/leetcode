# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            
            if node is None:
                return False
            
            curSum += node.val
            
            if node.left is None and node.right is None:
                return curSum == targetSum
            
            leftSubTree = dfs(node.left, curSum)
            rightSubTree = dfs(node.right, curSum)
            
            return leftSubTree or rightSubTree
        
        return dfs(root, 0)