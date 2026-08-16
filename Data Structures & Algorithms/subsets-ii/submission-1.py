import bisect

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        def dfs(index: int, path: List[int]) -> None:
            results.append(path.copy())
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                    
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return results