class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0

        jumps = 0
        while r < n-1:
            f = 0
            for j in range(l, r+1):
                f = max(f, j+nums[j])

            l = r+1
            r = f
            jumps += 1

        return jumps