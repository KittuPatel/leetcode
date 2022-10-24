# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        queue = collections.deque([])
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            
            if len(queue) < k:
                queue.append(root.val)
            else:
                if abs(queue[0]-target) > abs(root.val-target):
                    queue.popleft()
                    queue.append(root.val)
                else:
                    return
                
            
            dfs(root.right)
            
        dfs(root)
        
        return queue