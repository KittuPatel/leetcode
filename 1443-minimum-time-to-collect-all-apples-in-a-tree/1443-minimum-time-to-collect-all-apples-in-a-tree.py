class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i: [] for i in range(n)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        def dfs(cur, parent):
            time = 0
            
            for child in adj[cur]:
                if child == parent:
                    continue
                    
                childTime = dfs(child, cur)
                
                if childTime or hasApple[child]:
                    time += 2 + childTime
                
            return time
                
                
        return dfs(0, -1)
                


