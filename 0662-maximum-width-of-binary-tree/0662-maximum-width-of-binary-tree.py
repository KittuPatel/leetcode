# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # [1], [3,2], [5, 3, None, 9]
        
        queue = collections.deque([[root, 1]]) # node, numID
        res = 0
        
        while queue:
            # keep track of first element in each level
            _, start_idx = queue[0]
            
            for i in range(len(queue)):
                node, numId = queue.popleft()
            
                if node.left:
                    queue.append([node.left, 2*numId])
                if node.right:
                    queue.append([node.right, 2*numId+1])
                
            res = max(res, numId-start_idx+1)
                
        return res