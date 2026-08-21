from typing import List
import heapq
import itertools

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        whole = sum(nums)
        if whole % 2 != 0:
            return False
            
        nums.sort(reverse=True)
        half = whole // 2
        n = len(nums)
        
        # Tie-breaker to prevent the heap from trying to compare the sets
        counter = itertools.count()
        
        # Initialize the heap with a single starting state
        # Format: (-current_sum, tie_breaker, current_sum, used_set)
        max_heap = [(-0, next(counter), 0, set())]

        while max_heap:
            _, _, current_sum, used = heapq.heappop(max_heap)

            if current_sum == half:
                return True
            
            for i in range(n):
                if i not in used:
                    if nums[i] <= (half - current_sum):
                        new_used = used.copy()
                        new_used.add(i)
                        
                        new_sum = current_sum + nums[i]
                        heapq.heappush(
                            max_heap, 
                            (-new_sum, next(counter), new_sum, new_used)
                        )

        return False