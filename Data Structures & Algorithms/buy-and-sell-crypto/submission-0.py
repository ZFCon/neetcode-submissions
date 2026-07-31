class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        result = 0

        i = 0
        while i+1 < n:
            p1 = prices[i]
            p2 = max(prices[i+1:])
            result = max(result, p2-p1)
            i += 1 

        return result