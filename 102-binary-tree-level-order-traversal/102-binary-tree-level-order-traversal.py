# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            qLen = len(queue)
            # qLen is ensuring we iterate one level at a time
            level = []
            for _ in range(qLen):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                res.append(level)
            
        
        return res
            
            