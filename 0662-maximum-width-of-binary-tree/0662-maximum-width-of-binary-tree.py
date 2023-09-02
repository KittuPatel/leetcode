# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque([(root, 1)])
        res = 0
        
        while q:
            startIdx = q[0][1]
            for i in range(len(q)):
                node, numId = q.popleft()
                if node.left:
                    q.append((node.left, 2*numId))
                if node.right:
                    q.append((node.right, 2*numId+1))
                
            res = max(res, numId - startIdx+1)
            
        return res
            
            
        