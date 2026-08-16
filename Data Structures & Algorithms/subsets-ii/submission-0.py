import bisect

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()
        
        def dfs(index: int, path: List[int]) -> None:
            tuple_path = tuple(path)
            if index > len(nums) or tuple_path in visited:
                return

            results.append(path)
            visited.add(tuple_path)

            for i in range(index, len(nums)):
                new_path = path.copy()
                bisect.insort(new_path, nums[i])
                dfs(i+1, new_path)

        dfs(0, [])
        return results