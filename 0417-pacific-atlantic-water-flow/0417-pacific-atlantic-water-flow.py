class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs 

        ROWS, COLS = len(heights), len(heights[0])
        pacSet, atlSet = set(), set()
        res = []
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
               r < 0 or c < 0 or c == COLS or r == ROWS or heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if 0 <= newR < ROWS and 0 <= newC < COLS:  # Check bounds here
                    dfs(newR, newC, visit, heights[r][c])
                
        
        # do dfs for first row (pac) and last row (atl)
        for c in range(COLS):
            dfs(0, c, pacSet, heights[0][c])
            dfs(ROWS-1, c, atlSet, heights[ROWS-1][c])
            
        # do dfs for first col (pac) and last col (atl)
        for r in range(ROWS):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, COLS-1, atlSet, heights[r][COLS-1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacSet and (r, c) in atlSet:
                    res.append([r, c])
                    
        return res
        