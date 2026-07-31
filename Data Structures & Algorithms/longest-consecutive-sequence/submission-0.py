class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        result = 0

        previous = None
        counter = 0
        for num in nums:
            if previous is None:
                counter += 1
            elif (num - previous) == 1:
                counter += 1
            else:
                counter = 1
            previous = num
            result = max(result, counter)

        return result