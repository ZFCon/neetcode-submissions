class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = [len(nums)]
        visited = set()

        def dfs(path: List[int]) -> None:
            if len(path) == n[0]:
                results.append(path.copy())
                return
    
            for i in range(n[0]):
                if i not in visited:
                    visited.add(i)
                    path.append(i)
                    dfs(path)
                    path.pop()
                    visited.remove(i)

        dfs([])
        return [[nums[i] for i in result] for result in results]
            