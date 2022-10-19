# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root 
        while curr and curr.left: 
            curr = curr.left 
            
        self.dfs(root, None, None)
        
        return curr 
            
    
    def dfs(self, curr, par, sib): 
        if not curr: 
            return 
        
        self.dfs(curr.left, curr, curr.right)
        self.dfs(curr.right, None, None) 
        
        
        curr.left = sib 
        curr.right = par 
                
            