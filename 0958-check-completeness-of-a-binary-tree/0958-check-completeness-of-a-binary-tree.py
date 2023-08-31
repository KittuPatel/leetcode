# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node:
                    res.append(None)
                else:
                    if res and res[-1] == None:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
                    
        return True
