class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0

        grids = [[0] * n for  _ in range(m)]
        grids[0][0] = 1

        for x in range(m):
            for y in range(n):
                if x  == 0 and y == 0:
                    continue
                before_up = 0
                if x > 0:
                    before_up = grids[x-1][y]
                before_left = 0
                if y > 0:
                    before_left = grids[x][y-1]
                grids[x][y] = before_up + before_left 


        return grids[m-1][n-1]