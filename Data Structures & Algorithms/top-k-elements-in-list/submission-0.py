from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_nums = sorted(set(nums), key=lambda x: counter[x], reverse=True)

        return sorted_nums[:k]