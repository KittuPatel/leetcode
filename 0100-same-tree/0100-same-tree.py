# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # bfs
        
        def bfs(p,q):
            deque = collections.deque()
            deque.append((p, q))
            
            while deque:
                p, q = deque.popleft()
                if p and q and p.val == q.val:
                    deque.append((p.left, q.left))
                    deque.append((p.right, q.right))
                
                elif p or q:
                    return False
            
            return True
        
        return bfs(p, q)
            
                