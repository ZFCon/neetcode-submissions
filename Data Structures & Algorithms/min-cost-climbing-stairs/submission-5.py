from typing import List
from collections import deque

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        q = deque([(1, 0), (0, 0)])
        n = len(cost)
        # Expanded memo to n + 1 to account for reaching the top
        memo = {i: float("inf") for i in range(n + 1)}
        
        min_cost = float("inf")

        while q:
            i, c = q.popleft()

            # Reached the top of the floor
            if i >= n:
                min_cost = min(min_cost, c)
                continue
            
            # If we've already found a cheaper or equal way to this step, skip
            if memo[i] <= c:
                continue

            memo[i] = c

            # Look ahead to see the cost of the next potential steps
            # Default to 0 if the step jumps past the last stair
            q.append((i + 1, c + cost[i]))
            q.append((i + 2, c + cost[i]))
            
        return min_cost