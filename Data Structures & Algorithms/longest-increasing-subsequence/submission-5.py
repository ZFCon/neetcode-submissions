from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # memo[i] will store the max sequence length STARTING at index i
        memo = {}
        
        # We start at index 0, finish it fully to the end, then index 1, etc.
        for i in range(n):
            if i in memo:
                continue
                
            # Stack stores tuples of: (current_index, children_visited_flag)
            stack = [(i, False)]
            
            while stack:
                curr, visited = stack.pop()
                
                if visited:
                    # We have fully explored all paths after this index.
                    # Now we can safely calculate the max counter for this index.
                    if curr not in memo:
                        max_len = 1
                        for j in range(curr + 1, n):
                            if nums[j] > nums[curr]:
                                # We add 1 to the longest path of a valid child
                                max_len = max(max_len, 1 + memo[j])
                        memo[curr] = max_len
                else:
                    # If we've already solved this index via another path, skip it
                    if curr in memo:
                        continue
                        
                    # 1. Put the current node back on the stack marked as visited (True)
                    # It will sit on the stack and wait until all children finish.
                    stack.append((curr, True))
                    
                    # 2. Push all valid future children to the stack.
                    # We iterate backwards so the closest index is popped first, 
                    # ensuring we go strictly left-to-right down the array.
                    for j in range(n - 1, curr, -1):
                        if nums[j] > nums[curr] and j not in memo:
                            stack.append((j, False))

        # The result is the maximum sequence length found starting from ANY index
        return max(memo.values())