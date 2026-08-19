from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        # DFS now has one simple job: Turn connected 'O's into 'S' (Safe)
        def dfs(x: int, y: int) -> None:
            # Base cases: out of bounds, or NOT an "O"
            if x < 0 or y < 0 or x >= n or y >= m or board[x][y] != "O":
                return
            
            # Mark it as Safe
            board[x][y] = "S"
            
            # Spread to neighbors
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        # 1. ONLY launch DFS from the outer borders of the board.
        # This guarantees we only mark "O"s that are NOT surrounded.
        for x in range(n):
            for y in range(m):
                if board[x][y] == "O" and (x == 0 or x == n-1 or y == 0 or y == m-1):
                    dfs(x, y)
                    
        # 2. Final Sweep:
        # - Any "O" left on the board was completely surrounded. Flip to "X".
        # - Any "S" was connected to the border. Revert to "O".
        for x in range(n):
            for y in range(m):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "S":
                    board[x][y] = "O"