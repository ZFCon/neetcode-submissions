from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # memo[(prev, i)] will store the max sequence length for this state
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
            memo[(prev, i)] = counter

            # Branch 1: Skip the current number
            stack.append([counter, prev, i+1])
            
            # Branch 2: Take the current number
            if nums[i] > prev:
                stack.append([counter+1, nums[i], i+1])
                
        return result