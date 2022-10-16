# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            q = collections.deque([root])
            res = []
            while q:
                qLen = len(q)
                level = []
                for _ in range(qLen):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                
                if q:
                    res.append(level)
            
            return res
        
        res = bfs(root)
        output = res[-1]
        
        return sum(output)
                    
            