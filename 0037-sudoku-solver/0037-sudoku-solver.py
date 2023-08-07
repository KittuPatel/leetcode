class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def safe(row, col, numToFill, board):
            for i in range(9):
                if board[row][i] == numToFill:
                    return False
                if board[i][col] == numToFill:
                    return False
                
                if board[3 * (row//3) + i // 3][3 * (col//3) + i % 3] == numToFill:
                    return False
            return True
        
        def solve(board):
            for row in range(9):
                for col in range(9):
                    
                    if board[row][col] == ".":
                        for numToFill in range(1, 10):
                            numToFill = str(numToFill)
                            
                            if safe(row, col, numToFill, board):
                                board[row][col] = numToFill
                                if solve(board):
                                    return True
                                board[row][col] = "."
                        return False
            return True
        
        solve(board)