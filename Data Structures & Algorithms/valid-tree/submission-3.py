class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        paths = [[] for _ in range(n)]
        visited = set()

        for i, to in edges:
            paths[i].append(to)
            paths[to].append(i)
        
        def dfs(index: int, parent: int) -> bool:
            if index in visited:
                return False

            visited.add(index)

            for i in paths[index]:
                if i == parent:
                    continue

                result = dfs(i, index)
                if not result:
                    return False

            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n