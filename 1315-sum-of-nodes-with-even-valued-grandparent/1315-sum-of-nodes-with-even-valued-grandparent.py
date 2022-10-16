# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        sum = 0
    
        def dfs(child, parent, grandParent):
            nonlocal sum
            
            if not child:
                return 

            if grandParent!= None and grandParent.val%2==0:
                sum += child.val

            # Child, Parent and Grand Parent
            dfs(child.left, child, parent)
            dfs(child.right, child, parent)
        
        dfs(root, None, None)
        return sum
        
        

#         self.sum=0
        
#         self.dfs(root,None, None)        
#         return self.sum
    
#     def dfs(self,child, parent, grandParent):
#         if not child:
#             return 
        
#         if grandParent!= None and grandParent.val%2==0:
#             self.sum += child.val
            
#         # Child, Parent and Grand Parent
#         self.dfs(child.left, child, parent)
#         self.dfs(child.right, child, parent)