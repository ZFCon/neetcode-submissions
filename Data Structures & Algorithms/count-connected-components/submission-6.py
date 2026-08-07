class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        paths = [[] for _ in range(n)]
        counter = 0

        for f, t in edges:
            paths[f].append(t)
            paths[t].append(f)

        visited = set()

        def dfs(index: int, parent: int) -> None:
            if index in visited:
                return
            visited.add(index)

            for i in paths[index]:
                if i == parent:
                    continue
                
                dfs(i, index)

        for i in range(n):
            if i not in visited:
                dfs(i, i)
                counter += 1

        return counter