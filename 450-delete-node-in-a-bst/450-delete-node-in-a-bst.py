# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMinNodefromRightSubTree(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
    
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: leaf node
            if root.left is None and root.right is None:
                root = None
            
            # case 2: one node          
            elif root.left is None:
                root = root.right
            
            elif root.right is None:
                root = root.left
            
            # case 3: two nodes
            # 1 -> assign root to smallest element
            # 2 -> remove smallest element from right subtree
            else:
                temp = self.findMinNodefromRightSubTree(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
                
            
            