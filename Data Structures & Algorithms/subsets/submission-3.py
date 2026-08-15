class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(current: int, path: List[int]) -> None:
            if current > len(nums):
                return

            results.append(path)
            for i in range(current, len(nums)):
                dfs(i+1, path+[nums[i]])
        

        dfs(0, [])
        return results