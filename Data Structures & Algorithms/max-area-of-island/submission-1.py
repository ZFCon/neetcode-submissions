class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or not grid[x][y]:
                return 0

            grid[x][y] = 0
            return dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1) + 1
            

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    result = max(result, dfs(x, y))
                    
        return result