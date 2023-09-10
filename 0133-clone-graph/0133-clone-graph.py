"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        visited = {}
        
        def dfs(org_node):
            if org_node not in visited:
                cloned_node = Node(org_node.val, [])
                visited[org_node] = cloned_node

                for neighbor in org_node.neighbors:
                    cloned_neighbor = dfs(neighbor)
                    cloned_node.neighbors.append(cloned_neighbor)
                
            return visited[org_node]
            
        
        return dfs(node)