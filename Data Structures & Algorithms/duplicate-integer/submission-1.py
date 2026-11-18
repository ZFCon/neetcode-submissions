class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        finder = set()

        for num in nums:
            if num in finder:
                return True
            finder.add(num)

        return False