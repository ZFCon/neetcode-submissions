from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Base cases: out of bounds or water (0)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            # Mark as visited by sinking the island
            grid[r][c] = 0
            
            # Explore all 4 adjacent directions
            return (1 + dfs(r-1, c) + 
                        dfs(r+1, c) + 
                        dfs(r, c-1) + 
                        dfs(r, c+1))

        # Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area