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
            
        def dfs(root, parent, sibling):
            if not root:
                return
            
            dfs(root.left, root, root.right)
            dfs(root.right, None, None)
            
            root.left = sibling
            root.right = parent
            
        dfs(root, None, None)
        
        return curr
            
                
            