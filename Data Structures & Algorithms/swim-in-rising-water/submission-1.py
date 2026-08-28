import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # min heap to know the next step: (elevation, -x, -y)
        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        max_time = 0
        
        while min_heap:
            elevation, neg_x, neg_y = heapq.heappop(min_heap)
            
            # Convert back to positive x and y
            x, y = -neg_x, -neg_y
            
            # The water level is bottlenecked by the highest peak crossed
            max_time = max(max_time, elevation)
            
            if x == n - 1 and y == n - 1:
                return max_time
                
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    # Push negative coordinates to prioritize the bottom-right
                    heapq.heappush(min_heap, (grid[nx][ny], -nx, -ny))