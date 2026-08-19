class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        q = deque()
        result = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        for x in range(n):
            for y in range(m):
                if grid[x][y] == ROTTEN:
                    q.append((x, y))

        while q:
            rottened = False
            for _ in range(len(q)):
                x, y = q.popleft()    

                for xd, yd in directions:
                    nx, ny = x+xd, y+yd

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    
                    if grid[nx][ny] == FRESH:
                        q.append((nx, ny))
                        grid[nx][ny] = ROTTEN
                        rottened = True

            if rottened:
                result += 1
        
        for x in range(n):
            for y in range(m):
                if grid[x][y] == FRESH:
                    return -1

        return result