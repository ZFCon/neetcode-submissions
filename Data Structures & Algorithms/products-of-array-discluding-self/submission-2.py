class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1]*n
        after = [1]*n

        k = 1
        for i in range(n):
            before[i] = k
            k *= nums[i]

        k = 1
        for i in reversed(range(n)):
            after[i] = k
            k *= nums[i]

        return [before[i] * after[i] for i in range(n)]

        
