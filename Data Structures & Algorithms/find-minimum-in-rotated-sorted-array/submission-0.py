class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return -1
        
        l, r = 0, n-1
        result = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            m = (l+r) // 2
            result = min(result, nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        return result

    