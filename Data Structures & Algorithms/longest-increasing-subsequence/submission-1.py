class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        result = 0

        def dfs(i: int, curr: int) -> int:
            # FIX 1: If we run out of numbers, we can add 0 to our sequence
            if i >= n:
                return 0

            if (i, curr) in memo:
                return memo[(i, curr)]

            # FIX 2: Remove the unused 'for j' loop. Just check the current 'i'.
            # Branch A: We skip nums[i]
            res = dfs(i + 1, curr)
            
            # Branch B: We take nums[i] (only if it's bigger than our current number)
            if curr < nums[i]:
                # FIX 3: Add 1 to count the number we just took
                res = max(res, 1 + dfs(i + 1, nums[i]))

            memo[(i, curr)] = res
            
            return res

        for i in range(n):
            # FIX 4: Add 1 here too, because we are counting nums[i] as our first number
            result = max(result, 1 + dfs(i + 1, nums[i]))

        return result