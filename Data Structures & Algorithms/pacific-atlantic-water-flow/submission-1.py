class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        visited_p = set()
        visited_a = set()
        n, m = len(heights), len(heights[0])
        stack = []

        # Add first row (Pacific) and bottom row (Atlantic)
        for c in range(m):
            # First row - Pacific
            stack.append((0, c, 'p', heights[0][c]))
            
            # Bottom row - Atlantic
            stack.append((n - 1, c, 'a', heights[n - 1][c]))

        # Add first col (Pacific) and last col (Atlantic)
        for r in range(n):
            # First col - Pacific
            stack.append((r, 0, 'p', heights[r][0]))
            
            # Last col - Atlantic
            stack.append((r, m - 1, 'a', heights[r][m - 1]))

        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            x, y, ocean, height = stack.pop()

            # 1. Check if already visited in this type of ocean. Skip if true, mark if false.
            if ocean == 'p':
                if (x, y) in visited_p:
                    continue
                visited_p.add((x, y))
            elif ocean == 'a':
                if (x, y) in visited_a:
                    continue
                visited_a.add((x, y))

            # 2. Go in all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Make sure the new coordinates are within grid bounds
                if 0 <= nx < n and 0 <= ny < m:
                    
                    # 3. If neighbor's height is equal or more than the current height
                    if heights[nx][ny] >= height:
                        
                        # 4. Use the max height between the two 
                        new_height = max(height, heights[nx][ny])
                        
                        stack.append((nx, ny, ocean, new_height))

        # 5. Format the result to find boxes visited by BOTH oceans
        result = []
        for r in range(n):
            for c in range(m):
                if (r, c) in visited_p and (r, c) in visited_a:
                    result.append([r, c])
                    
        return result