class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        counter = 0
        visited = set()

        def dfs(x: int, y: int) -> None:
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0" or (x, y) in visited:
                return
            else:
                visited.add((x, y))
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and (x, y) not in visited:
                    dfs(x, y)
                    counter += 1

        return counter