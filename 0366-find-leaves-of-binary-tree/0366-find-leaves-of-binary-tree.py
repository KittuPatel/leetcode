# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = collections.defaultdict(list)
        
        def postorder(root, height):
            if not root:
                return height
            
            left = postorder(root.left, height)
            right = postorder(root.right, height)
            
            height = max(left, right)
            
            res[height].append(root.val)
            
            return height + 1
        
        postorder(root, 0)
        
        return res.values()