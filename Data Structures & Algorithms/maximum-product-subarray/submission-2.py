class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = float("-inf")
        n = len(nums)
        lp = 1
        rp = 1

        for i in range(n):
            lp *= nums[i]
            rp *= nums[n-1-i]

            result = max([lp, rp, result])
            if lp == 0:
                lp = 1
            if rp == 0:
                rp = 1

        return result