# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            # res = []
            levels = 0
            q = collections.deque([root])
            
            while q:
                qLen = len(q)
                # temp = 0
                for _ in range(qLen):
                    node = q.popleft()
                    if node:
                        q.append(node.left)
                        q.append(node.right)
                        
                if q:
                    levels += 1
                    
            return levels
        
        return bfs(root)
                    