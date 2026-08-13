import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        nums = []

        i = j = 0

        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
        nums.extend(nums1[i:])
        nums.extend(nums2[j:])

        total_length = len(nums)
        mid = total_length // 2

        if total_length % 2 == 0:
            # Even total length: average the two middle elements
            return (nums[mid - 1] + nums[mid]) / 2.0
        else:
            # Odd total length: return the exact middle element
            return float(nums[mid])
