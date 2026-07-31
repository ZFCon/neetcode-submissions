class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        i = 0
        while i <= n:
            if i == n or i != nums[i]:
                break
            i += 1


        return i

