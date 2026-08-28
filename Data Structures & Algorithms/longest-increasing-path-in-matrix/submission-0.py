from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # memo now only needs to hold x and y
        memo = {}
        
        def dfs(x, y, prev):
            # check boundaries
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return 0
                
            # if you reach a smaller or equal and end
            if matrix[x][y] <= prev:
                return 0
                
            # Check if this exact cell is in our memo
            if (x, y) in memo:
                return memo[(x, y)]
                
            # Branch out in all 4 directions
            left = dfs(x, y - 1, matrix[x][y])
            right = dfs(x, y + 1, matrix[x][y])
            up = dfs(x - 1, y, matrix[x][y])
            down = dfs(x + 1, y, matrix[x][y])
            
            # calculate the result for this step
            result = 1 + max(left, right, up, down)
            
            # save it in the memo using only the coordinates
            memo[(x, y)] = result
            return result
            
        max_result = 0
        
        # start a dfs from each point
        for i in range(rows):
            for j in range(cols):
                current_len = dfs(i, j, float("-inf"))
                
                if current_len > max_result:
                    max_result = current_len
                    
        return max_result