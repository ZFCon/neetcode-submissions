from typing import List
from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)

        @cache
        def dfs(left: int, right: int):
            if left == right-1:
                return 0
                
            max_coins = 0
            for i in range(left+1, right):
                coins = (dfs(left, i) + dfs(i, right) + (nums[left] * nums[i] * nums[right]))
                max_coins = max(max_coins, coins)
                    
            return max_coins
            
        return dfs(0, n-1)