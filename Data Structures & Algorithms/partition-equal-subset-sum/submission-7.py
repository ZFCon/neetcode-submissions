from typing import List
import heapq

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        whole = sum(nums)
        if whole % 2 != 0:
            return False
        nums.sort(reverse=True)

        half = whole // 2
        n = len(nums)
        
        # Replaced deque with a list for the heap. 
        # Format is (negative_sum_for_max_heap, actual_sum, last_index)
        q = [(-0, 0, -1)]

        while q:
            # Replaced q.popleft() with heapq.heappop()
            _, current_sum, last_index = heapq.heappop(q)

            if current_sum == half:
                return True
            
            # Start loop at last_index + 1 to prevent going backward
            for i in range(last_index + 1, n):
                # The 'if i not in used:' check is removed
                if nums[i] <= (half - current_sum):
                    # No more copying sets, just push the new sum and current index 'i'
                    heapq.heappush(q, (-(current_sum + nums[i]), current_sum + nums[i], i))

        return False