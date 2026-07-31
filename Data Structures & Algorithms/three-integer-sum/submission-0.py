from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        n = len(nums)
        results = set()

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                num_k = -(nums[i] + nums[j])

                if num_k in counter:
                    if num_k == nums[i] and counter[num_k] < 2 :
                        continue
                    if num_k == nums[j] and counter[num_k] < 2 :
                        continue
                    if num_k == nums[j] and num_k == nums[i] and counter[num_k] < 3 :
                        continue
                    results.add(tuple(sorted((nums[i], nums[j], num_k))))

        return list(results)