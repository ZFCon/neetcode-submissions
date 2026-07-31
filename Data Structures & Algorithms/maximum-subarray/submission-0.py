class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        q = [[0, 1]] 
        result = float("-inf")

        while q:
            i, j = q.pop()
            amount = sum(nums[i:j])

            if i >= j or j > n:
                continue

            result = max(result, amount)


            if amount < 0:
                q.append([j, j+1])
            else:
                q.append([i, j+1])

        return result