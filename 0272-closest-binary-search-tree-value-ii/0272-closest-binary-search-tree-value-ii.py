# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
            return res
        
        dfs(root)
        
        l = 0
        r = k - 1
        while r <= len(res) - 2:
            if abs(res[r+1] - target) < abs(res[l] - target):
                l += 1
                r += 1
            else:
                return res[l: r+1]
            
        return res[l: r+1]
        
        
        
#         l
        
#         while right <= len(self.nodes) - 2:
#             if abs(self.nodes[right + 1] - target) < abs(self.nodes[left] - target):
#                 left += 1
#                 right += 1
#             else:
#                 return self.nodes[left: right + 1]
        
#         return self.nodes[left: right + 1]
        
#  O (NLOGN) AND O(N)
        #         res = []
#         def dfs(root):
#             if root:
#                 dfs(root.left)
#                 res.append(root.val)
#                 dfs(root.right)
#             return res
        
#         dfs(root)
        
#         res.sort(key=lambda x: abs(target - x))
        
#         return res[:k]


