import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = min(len(nums1), len(nums2))
        nums = []

        for _ in range(n):
            if nums1[0] <= nums2[0]:
                nums.append(nums1.pop(0))
                nums.append(nums2.pop(0))
            else:
                nums.append(nums2.pop(0))
                nums.append(nums1.pop(0))

        nums.extend(nums1)
        nums.extend(nums2)

        return statistics.median(nums)
