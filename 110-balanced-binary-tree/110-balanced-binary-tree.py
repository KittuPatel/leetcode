# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # assume height of empty tree as -1.
            if root is None:
                return [True, -1]
            
            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)
            
            # now determine from subtree root node if left and right is balanced
            isBalanced = leftSubTree[0] and rightSubTree[0] and abs(leftSubTree[1] - rightSubTree[1]) <= 1
            
            return [isBalanced, max(leftSubTree[1], rightSubTree[1]) + 1]
        
        
        
        return dfs(root)[0]          