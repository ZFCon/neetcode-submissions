from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        
        # 1. using deque create a q
        q = deque()
        
        # 2. which you fill with all the gates (0)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 3. and then you pop a gate from left
        while q:
            r, c = q.popleft()
            
            # 4. look at all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries first
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                    
                # 5. if it's a number you simply skip as long as it's not inf
                # (This skips obstacles (-1), gates (0), and already visited spaces)
                if grid[nr][nc] != INF:
                    continue
                    
                # 6. if it's an inf number you add the distance from the gate
                grid[nr][nc] = grid[r][c] + 1
                
                # 7. and append all direction again to the right 
                # (by adding this new cell to the queue)
                q.append((nr, nc))