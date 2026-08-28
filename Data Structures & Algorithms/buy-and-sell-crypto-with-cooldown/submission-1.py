from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dfs(index, coin):
            # whenever we reach the end we calculate current profit
            if index >= len(prices):
                return 0
                
            if (index, coin) in memo:
                return memo[(index, coin)]
                
            # if you don't have coin
            if coin == 0:
                # either take coin now and go to the next
                buy = dfs(index + 1, 1) - prices[index]
                # or you don't and go to the next
                skip = dfs(index + 1, 0)
                
                memo[(index, coin)] = max(buy, skip)
                
            # if we have a coin
            else:
                # either sell it and go after next (index + 2 for cooldown)
                sell = dfs(index + 2, 0) + prices[index]
                # or we don't sell and go to the next
                skip = dfs(index + 1, 1)
                
                memo[(index, coin)] = max(sell, skip)
                
            return memo[(index, coin)]
            
        return dfs(0, 0)