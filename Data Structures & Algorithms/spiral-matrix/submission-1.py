from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
            
        m = len(matrix)
        n = len(matrix[0])
        
        # 1. Create 4 constants for our directions (row_change, col_change)
        RIGHT = (0, 1)   # Stay on same row, move 1 column right
        DOWN = (1, 0)    # Move 1 row down, stay on same column
        LEFT = (0, -1)   # Stay on same row, move 1 column left
        UP = (-1, 0)     # Move 1 row up, stay on same column
        
        # 2. Sort them in the exact spiral sequence
        DIRECTIONS = [RIGHT, DOWN, LEFT, UP]
        
        visited = set()
        result = []
        
        r, c = 0, 0
        current_dir = 0  # Start by moving RIGHT (index 0)
        
        # We know exactly how many tiles to visit (m * n)
        for _ in range(m * n):
            # Record the current tile
            result.append(matrix[r][c])
            visited.add((r, c))
            
            # "Look ahead" to see where our current direction takes us
            next_r = r + DIRECTIONS[current_dir][0]
            next_c = c + DIRECTIONS[current_dir][1]
            
            # Check if the next tile hits a wall (bounds) OR a visited tile
            hit_wall = next_r < 0 or next_r >= m or next_c < 0 or next_c >= n
            hit_visited = (next_r, next_c) in visited
            
            if hit_wall or hit_visited:
                # "Go back and then go to the direction right after"
                # We turn 90 degrees by advancing our direction index
                current_dir = (current_dir + 1) % 4
                
                # Recalculate our next step using the new direction
                next_r = r + DIRECTIONS[current_dir][0]
                next_c = c + DIRECTIONS[current_dir][1]
                
            # Officially take the step to the next valid tile
            r, c = next_r, next_c
            
        return result