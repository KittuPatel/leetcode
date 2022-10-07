# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.dfs(root, res)
#         return res
    
#     def dfs(self, root, res):
#         if root:
#             self.dfs(root.left, res)
#             self.dfs(root.right, res)
#             res.append(root.val)
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
 
        # return if the tree is empty
        if root is None:
            return

        # create an empty stack and push the root node
        stack = deque()
        stack.append(root)

        # create another stack to store postorder traversal
        out = deque()

        # loop till stack is empty
        while stack:

            # pop a node from the stack and push the data into the output stack
            curr = stack.pop()
            out.append(curr.val)

            # push the left and right child of the popped node into the stack
            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)
        res = []
        # print postorder traversal
        while out:
            node = out.pop()
            res.append(node)
        
        return res
        