class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder = {}

        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in finder:
                return sorted([i, finder[new_target]])
            finder[nums[i]] = i
            