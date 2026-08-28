from collections import deque
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Start t at the elevation of the first cell (water can't flow until at least this time)
        t = grid[0][0]
        
        q = deque([(0, 0)])
        visited = {(0, 0)}
        
        # Outer loop for time ticks
        while True:
            processed_any = True
            
            # "While inside while": instantly process all cells reachable at the current time t
            while processed_any:
                processed_any = False
                
                # "Go over the whole q"
                for _ in range(len(q)):
                    x, y = q.popleft()
                    
                    # "Reach at most the farthest land that equal or less than current t"
                    if grid[x][y] <= t:
                        processed_any = True # We found a valid move, meaning we might unlock more moves
                        
                        # Check if we reached the end
                        if x == n - 1 and y == n - 1:
                            return t
                            
                        # Expand neighbors
                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            
                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                # "And of course append to the q"
                                q.append((nx, ny))
                    else:
                        # This cell is too high for the current time t, put it back for later
                        q.append((x, y))
                        
            # "If all are visited [processed] then you go into another tick"
            t += 1