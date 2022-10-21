# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            res=[]
            q = collections.deque([root])
            levelNum = 0
            while q:
                qLen = len(q)
                level = []
                for _ in range(qLen):
                    node = q.popleft()
                    if node:
                        level.append(node.val)             
                        q.append(node.right)
                        q.append(node.left)
                        
                if q:
                    if levelNum % 2 != 0:
                        res.append(level)
                    else:
                        res.append(level[::-1])
                    levelNum += 1
                    
            return res
        
        return bfs(root)

    
