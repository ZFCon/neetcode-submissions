from typing import List
import heapq

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Min-heap stores tuples of (total_cost, current_index)
        # We start with the option to step on index 0 or index 1, both with 0 cost initially.
        pq = [(0, 0), (0, 1)] 
        
        # Visited set replaces the memo array. 
        # In Dijkstra's, the first time we visit a node, it is guaranteed to be the cheapest.
        visited = set()

        while pq:
            # Pop always gives us the path with the absolute lowest total_cost so far
            c, i = heapq.heappop(pq)

            if i >= n:
                # Because the heap sorts by cost, the first time we cross the finish line
                # it is mathematically impossible for any other path to be cheaper.
                return c
                
            if i in visited:
                continue
                
            visited.add(i)

            # Push the next steps to the heap. 
            # We must add the cost of the current stair we are standing on.
            if i + 1 <= n:
                heapq.heappush(pq, (c + cost[i], i + 1))
            if i + 2 <= n:
                heapq.heappush(pq, (c + cost[i], i + 2))

        return 0