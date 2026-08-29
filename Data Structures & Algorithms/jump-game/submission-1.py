from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        xheap = [[-(nums[0] + 0), 0]] # (priority, -index)
        # the priority (length_jump + index)

        visited = set()

        while xheap:
            _, index = heapq.heappop(xheap)
            index = -index

            for jump_length in range(1, nums[index] + 1):
                priority = (jump_length + index)
                next_index = (index+jump_length)

                if next_index >= n-1:
                    return True

                if next_index not in visited:
                    heapq.heappush(xheap, (-priority, -next_index))

            visited.add(index)

        return False