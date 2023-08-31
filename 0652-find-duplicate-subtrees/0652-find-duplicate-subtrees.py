# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        subtree_map = {}
        duplicates = []
        
        def dfs(node):
            if not node:
                return "#"
            
            subtree_id = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
            subtree_map[subtree_id] = 1+ subtree_map.get(subtree_id, 0)
            
            if subtree_map[subtree_id] == 2:
                duplicates.append(node)
        
            return subtree_id
        
        dfs(root)
        return duplicates