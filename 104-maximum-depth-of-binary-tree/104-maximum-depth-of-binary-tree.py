# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # solution 1 recursive DFS
#         if root is None:
#             return 0
        
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
        
#         return 1 + max(left, right)


        # solution 2
        # cur = root
        # while cur:
            
            
        # solution 3 - iterative BFS - ans is number of levels
        level = 0
        
        queue = collections.deque([root])
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if node:
                level += 1
        
        return level
        
        
        
        
        
        
        
        
        
        
        
        
        
        