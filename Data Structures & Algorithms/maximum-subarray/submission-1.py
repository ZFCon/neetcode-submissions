class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = float("-inf")

        i, j = 0, 1
        amount = 0
        while j <= n:
            amount += nums[j-1]
            result = max(result, amount)


            if amount < 0:
                i, j = j, j+1
                amount = 0
            else:
                i, j = i, j+1

        return result