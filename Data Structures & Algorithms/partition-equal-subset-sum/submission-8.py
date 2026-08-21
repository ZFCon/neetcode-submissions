from typing import List
import heapq

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        whole = sum(nums)
        if whole % 2 != 0:
            return False
            
        half = whole // 2
        if max(nums) > half:
            return False

        n = len(nums)
        nums.sort(reverse=True)
        memo = {}

        def dfs(index: int, current: int) -> bool:
            if current == half:
                return True
            elif index >= n or current > half:
                return False

            key = (index, current)
            if key in memo:
                return memo[key]

            result = dfs(index+1, current+nums[index]) or dfs(index+1, current)
            memo[key] = result

            return result
                        
                

    
        return dfs(0, 0)