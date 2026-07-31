class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            
            if counter[num] >= 1:
                return True
            counter[num] += 1

        return False