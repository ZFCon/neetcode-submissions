class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(path: List[int]) -> None:
            if len(path) == len(nums):
                results.append(path)
                return

            for i in range(len(nums)):
                if i not in path:
                    dfs(path+[i]) 

        dfs([])
        return [[nums[i] for i in result] for result in results]
            