class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = {node: set() for node in range(1, n+1)}
        edges = {}
        for s, t, w in times:
            edges[(s, t)] = w
            nodes[s].add(t)

        visited = {i: float("inf") for i in range(1, n+1)}
        def dfs(node: int, path: int) -> int:
            if visited[node] <= path:
                return

            visited[node] = path

            sorted_neighbors = sorted(nodes[node], key=lambda t: edges[(node, t)])
            for t in sorted_neighbors:
                dfs(t, path+edges[(node, t)])

        dfs(k, 0)
        result = max(visited.values())
        return int(result) if result != float("inf") else -1