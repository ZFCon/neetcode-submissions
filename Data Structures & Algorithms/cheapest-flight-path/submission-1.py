from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make adj list with the flights 
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
            
        # Add a memoization dictionary to prevent Time Limit Exceeded
        memo = {}
        
        # make a dfs that add 1 with each stop
        def dfs(node, stops):
            if node == dst:
                return 0
                
            # If we exceed max allowed stops, this path is invalid
            if stops > k:
                return float('inf')
                
            if (node, stops) in memo:
                return memo[(node, stops)]
                
            min_price = float('inf')
            
            # Explore all outgoing flights
            for neighbor, price in adj[node]:
                # Take the minimum price of all valid paths
                min_price = min(min_price, price + dfs(neighbor, stops + 1))
                
            memo[(node, stops)] = min_price
            return min_price
            
        # so it will be something like return dfs(src, 0 stops)
        ans = dfs(src, 0)
        
        return ans if ans != float('inf') else -1