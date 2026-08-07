from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # memo[i] will store the max sequence length STARTING at index i
        memo = {}
        stack = [[0, float("-inf"), 0]]
        result = 0

        while stack:
            counter, prev, i = stack.pop()
            if i >= n:
                result = max(result, counter)
                continue

            if (prev, i) in memo and counter <= memo[(prev, i)]:
                continue
            memo[prev, i] = max(memo.get((prev, i), 0), counter)

            stack.append([counter, prev, i+1])
            if nums[i] > prev:
                stack.append([counter+1, nums[i], i+1])
            
            
        return result