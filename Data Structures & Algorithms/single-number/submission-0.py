class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        previous = None
        seen = False
        for i in range(n):
            if previous is not None and nums[i] != nums[previous]:
                return nums[previous]
            elif previous is not None and nums[i] == nums[previous]:
                previous = None
            else:
                previous = i

        return nums[previous]
            