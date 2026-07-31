class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        q = [0]
        while q:
            i = q.pop()
            if i >= n-1:
                return True
            for j in range(1, nums[i]+1):
                q.append(i+j)

        return False