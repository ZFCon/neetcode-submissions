class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i = 0  # Pointer for nums1
        j = 0  # Pointer for nums2
        n = len(nums1)
        m = len(nums2)

        # 1. Merge elements while both arrays have items left
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1  # Only advance pointer i
            else:
                nums.append(nums2[j])
                j += 1  # Only advance pointer j

        # 2. If nums1 has leftover elements, append them all
        while i < n:
            nums.append(nums1[i])
            i += 1

        # 3. If nums2 has leftover elements, append them all
        while j < m:
            nums.append(nums2[j])
            j += 1

        # 4. Calculate the median manually in O(1) time
        total_length = n + m
        mid = total_length // 2

        if total_length % 2 == 0:
            # Even total length: average the two middle elements
            return (nums[mid - 1] + nums[mid]) / 2.0
        else:
            # Odd total length: return the exact middle element
            return float(nums[mid])