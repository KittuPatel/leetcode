class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(row) for row in zip(*grid)]
        
        
        for r in range(n):
            for c in range(n):
                res += min(row_maxes[r], col_maxes[c]) - grid[r][c]
                
        return res
                
                