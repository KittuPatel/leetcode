class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        m = len(grid) # num of rows
        n = len(grid[0]) # num of cols
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        max_kill = 0
        
        # from left to right
        for i in range(m):
            num_of_enemy = 0
            for j in range(n):
                if grid[i][j] == '0':
                    dp[i][j] += num_of_enemy
                
                elif grid[i][j] == 'E':
                    num_of_enemy += 1
                
                elif grid[i][j] == 'W':
                    num_of_enemy = 0
        
        # from right to left
        for i in range(m):
            num_of_enemy = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == '0':
                    dp[i][j] += num_of_enemy
                
                elif grid[i][j] == 'E':
                    num_of_enemy += 1
                
                elif grid[i][j] == 'W':
                    num_of_enemy = 0
        

        # from up to bottom
        for j in range(n):
            num_of_enemy = 0
            for i in range(m):
                if grid[i][j] == '0':
                    dp[i][j] += num_of_enemy
                
                elif grid[i][j] == 'E':
                    num_of_enemy += 1
                
                elif grid[i][j] == 'W':
                    num_of_enemy = 0

        # from bottom to up
        for j in range(n):
            num_of_enemy = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == '0':
                    dp[i][j] += num_of_enemy
                
                elif grid[i][j] == 'E':
                    num_of_enemy += 1
                
                elif grid[i][j] == 'W':
                    num_of_enemy = 0
                
                max_kill = max(max_kill, dp[i][j])
        
        print(dp) # sanity check
        return max_kill

"""
we can replace 
'E' -> -1
'W' -> -2
'0' -> 0
in the original grid, then save space complexity
everytime we encounter grid[i][j] >= 0 it is/was a open space
as we can only place bomb in open space
if grid[i][j] == -1 ->enemy 
or grid[i][j] == -2 -> wall

Then counting max will return us the result.
"""