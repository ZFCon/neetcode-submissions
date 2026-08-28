from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        memo = {}
        
        def dfs(index, current_sum):
            # Base case: we successfully made the exact amount
            if current_sum == amount:
                return 1
                
            # Base case: we overshot, or we ran out of coin types
            if current_sum > amount or index == len(coins):
                return 0
                
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Branch 1: Use the current coin (index stays the same, we can use it again)
            # Branch 2: Skip the current coin and move to the next one (index + 1)
            combinations = (dfs(index, current_sum + coins[index]) + 
                            dfs(index + 1, current_sum))
                            
            memo[(index, current_sum)] = combinations
            return combinations
            
        return dfs(0, 0)