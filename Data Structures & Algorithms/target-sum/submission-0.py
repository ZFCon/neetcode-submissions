from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # 1. Early Mathematical Exit: instantly catch impossible targets
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
            
        # 2. Offload memoization to C-level
        @cache
        def dfs(index, current_sum):
            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0
                
            # You either add the current number to the sum or you subtract it
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])
            
            return add + subtract
            
        return dfs(0, 0)