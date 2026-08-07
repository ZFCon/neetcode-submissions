class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        result = float("-inf")
        # Added initial sum 0 to the stack
        stack = [[set(), 0, 0]] 
        
        # Dictionary to save the max money we had when reaching a specific state
        memo = {}

        while stack:
            visited, index, current_sum = stack.pop()

            # Create a state key based on the index and whether the first house was visited
            # (since visiting the first house changes the rules for the last house)
            state = (index, 0 in visited)
            
            # if we visited this index before with more (or equal) money, skip
            if state in memo and memo[state] >= current_sum:
                continue
                
            # save the current sum to memo for this state
            memo[state] = current_sum

            if index in visited or (index+1 < n and index+1 in visited):
                continue
            
            # edge case if we added first index as visited we add the last index as visited but we won't sum the end
            if index == n - 1 and 0 in visited:
                visited.add(index)
                current_sum_with = current_sum
            else:
                current_sum_with = current_sum + nums[index]
                
            # use the current_sum from the stack and compare to result and save the max
            current_sum_without = current_sum
            result = max(result, current_sum_with, current_sum_without)
            
            # go to next index with 2 roads
            # Road 1: append the current index to visited (summed current house -> go to after next house)
            if index + 2 < n:
                visited_with = visited.copy()
                visited_with.add(index)
                stack.append([visited_with, index + 2, current_sum_with])
                
            # Road 2: do not append (did not sum -> go to next house)
            if index + 1 < n:
                visited_without = visited.copy()
                stack.append([visited_without, index + 1, current_sum_without])
                
        return result