# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # pre order traversal
    def serialize(self, root):
        # convert tree to string
        res = []
        
        def dfs(root):
            if root is None:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(",")
        self.pointer = 0
        
        def dfs():
            if vals[self.pointer] == "N":
                self.pointer += 1
                return None
            
            node = TreeNode(int(vals[self.pointer]))
            self.pointer += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))