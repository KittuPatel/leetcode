# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        queue = collections.deque()
        col, row = 0, 0
        queue.append([col, row, root])
        
        while queue:
            for i in range(len(queue)):
                c, r, node = queue.popleft()
                
                if node.left:
                    queue.append([c-1, r+1, node.left])
                if node.right:
                    queue.append([c+1, r+1, node.right])
                
                ans.append([c, r, node.val])
        
        ans.sort()
        # [[-1,1,9],[0,0,3],[0,2,15],[1,1,20],[2,2,7]]
        
        res = [[ans[0][2]]]
        
        for i in range(1, len(ans)):
            if ans[i][0] == ans[i-1][0]:
                res[-1].append(ans[i][2])
            else:
                res.append([ans[i][2]])
                
        return res
            
            
                
        