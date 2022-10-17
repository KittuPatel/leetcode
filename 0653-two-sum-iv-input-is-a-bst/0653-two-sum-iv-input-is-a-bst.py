# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         res = []
#         def dfs(root):
#             nonlocal res
#             if root:
#                 dfs(root.left)
#                 res.append(root.val)
#                 dfs(root.right)
        
#         dfs(root)
        
        
#         hashset = set()
        
#         for num in res:
#             if k - num in hashset:
#                 return True
#             hashset.add(num)
            
#         return False


        def dfs(root, hashset):
            if not root:
                return False
            
            remaining = k - root.val
            if remaining in hashset:
                return True
            
            hashset.add(root.val)
            
            return dfs(root.left, hashset) or dfs(root.right, hashset)
        
        return dfs(root, set())
        
        
            