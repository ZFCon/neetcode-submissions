class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            best = max(dfs(i+1), dfs(i+2)+nums[i])

            memo[i] = best

            return best

        return dfs(0)