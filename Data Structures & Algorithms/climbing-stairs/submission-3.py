class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1]:
            return 1
            
        finder = {
            0: 1,
            1: 1,
        }

        for i in range(2, n+1):
            finder[i] = finder[i-1] + finder[i-2]

        return finder[n-1] + finder[n-2]