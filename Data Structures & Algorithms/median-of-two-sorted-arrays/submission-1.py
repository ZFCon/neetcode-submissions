import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = min(len(nums1), len(nums2))
        nums = []

        for i in range(n):
            if nums1[i] <= nums2[i]:
                nums.append(nums1[i])
                nums.append(nums2[i])
            else:
                nums.append(nums2[i])
                nums.append(nums1[i])

        nums.extend(nums1[n:])
        nums.extend(nums2[n:])

        return statistics.median(nums)
