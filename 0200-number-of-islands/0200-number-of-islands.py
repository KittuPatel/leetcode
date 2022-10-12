from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        number_of_islands = 0
        visited = set()
        
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            
            while q:
                row, col = q.popleft()
                
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
            
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    # do bfs
                    bfs(row, col)
                    number_of_islands += 1
                    
        return number_of_islands
    
                    
        