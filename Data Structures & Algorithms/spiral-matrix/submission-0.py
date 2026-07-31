from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        # Set up our 4 limiters
        top_limiter = 0
        bottom_limiter = len(matrix) - 1
        left_limiter = 0
        right_limiter = len(matrix[0]) - 1
        
        result = []
        
        # Keep spiraling inward until the limiters cross each other
        while top_limiter <= bottom_limiter and left_limiter <= right_limiter:
            
            # 1. Move Right (along the top boundary)
            for c in range(left_limiter, right_limiter + 1):
                result.append(matrix[top_limiter][c])
            top_limiter += 1  # Shrink the top boundary down
            
            # 2. Move Down (along the right boundary)
            for r in range(top_limiter, bottom_limiter + 1):
                result.append(matrix[r][right_limiter])
            right_limiter -= 1  # Shrink the right boundary left
            
            # Check if limiters crossed before doing the reverse trips
            if top_limiter <= bottom_limiter:
                # 3. Move Left (along the bottom boundary)
                for c in range(right_limiter, left_limiter - 1, -1):
                    result.append(matrix[bottom_limiter][c])
                bottom_limiter -= 1  # Shrink the bottom boundary up
                
            if left_limiter <= right_limiter:
                # 4. Move Up (along the left boundary)
                for r in range(bottom_limiter, top_limiter - 1, -1):
                    result.append(matrix[r][left_limiter])
                left_limiter += 1  # Shrink the left boundary right
                
        return result