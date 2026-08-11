from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m - 1

        while l <= r:
            mid = (l+r) // 2
            x = mid // m
            y = mid % m

            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False