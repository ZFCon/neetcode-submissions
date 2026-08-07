class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

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
                # 1. Skip stepping backward to the immediate parent
                if i == parent:
                    continue

                # 2. Pass current 'index' as the parent to the child call
                result = dfs(i, index)
                if not result:
                    return False

            return True

        # 3. Run DFS once starting from node 0 (using -1 as no parent)
        if not dfs(0, -1):
            return False

        # Ensure all nodes are connected in a single tree
        return len(visited) == n