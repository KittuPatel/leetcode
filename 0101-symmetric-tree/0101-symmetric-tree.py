# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(root):
            res = []
            q = collections.deque([root])
            
            while q:
                qLen = len(q)
                level = []
                
                for _ in range(qLen):
                    node = q.popleft()
                    if not node: 
                        level.append("N")
                    else:
                        level.append(node.val)
                    if node:
                        q.append(node.left)
                        q.append(node.right)
                        
                if q:
                    res.append(level)
                    
            return res
        
        
        res = bfs(root)
        print(res)
        
        for arr in res:
            print(arr, arr[::-1])
            if arr != arr[::-1]:
                return False
            
        return True
                        