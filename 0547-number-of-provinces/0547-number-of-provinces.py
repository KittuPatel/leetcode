class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [0] * len(isConnected)
        
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = 1
                    dfs(j)
        
        ans = 0
        for i in range(len(visited)):
            if not visited[i]:
                ans += 1
                dfs(i)
        
        return ans
        