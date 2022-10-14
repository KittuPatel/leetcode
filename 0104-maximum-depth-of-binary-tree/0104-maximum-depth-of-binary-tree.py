# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return 1 + max(left, right)
        
    
        return dfs(root)
        
#         def bfs():
#             q = collections.deque([root])
#             level = 0
#             while q:
#                 qLen = len(q)
#                 for _ in range(qLen):
#                     node = q.popleft()
#                     if node:
#                         q.append(node.left)
#                         q.append(node.right)
#                 if q:
#                     level += 1
                
#             return level
        
#         return bfs()
            
            