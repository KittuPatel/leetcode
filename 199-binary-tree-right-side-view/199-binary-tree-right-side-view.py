class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:    
        # dfs
        res = []
        
        def helper(root, level):
            if not root:
                return root
            
            if len(res) == level:
                res.append(root.val)
                
            # right first
            helper(root.right, level + 1)
            helper(root.left, level + 1)
            
            return root
            
        helper(root, 0)
        return res
    
        
        
        
        
        
        
        
        
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         q = deque([root])
        
#         while q:
#             rightSide = None
#             qLen = len(q)
#             for i in range(qLen):
#                 node = q.popleft()
#                 if node:
#                     rightSide = node
#                     q.append(node.left)
#                     q.append(node.right)
                    
#             if rightSide:
#                 res.append(rightSide.val)
                
#         return res
