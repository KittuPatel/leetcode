# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            
#         if root is None:
#             return 0

#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)

#         return 1 + max(left, right)
        
#         iterative bfs

        res = []
        q = collections.deque()
        q.append(root)    
        
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                res.append(level)
                
        return len(res)

        