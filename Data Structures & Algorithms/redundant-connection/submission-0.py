from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def create_map(edges_sub: List[List[int]]) -> dict:
            m = {}
            for i, e in edges_sub:
                m[i] = m.get(i, [])
                m[i].append(e)

                m[e] = m.get(e, [])
                m[e].append(i)
            return m

        def has_cycle(m: dict) -> bool:
            visited = set()

            def dfs(node: int, parent: int) -> bool:
                if node in visited:
                    return True

                visited.add(node)
                
                for i in m[node]:
                    if i == parent:
                        continue
                        
                    if dfs(i, node):
                        return True

                visited.remove(node)
                return False

            # Check every component in the graph for a cycle
            for node in m.keys():
                if node not in visited:
                    if dfs(node, node):
                        return True
            return False

        # Loop through edges in reverse (from last to first)
        for i in range(len(edges) - 1, -1, -1):
            # Temporarily remove one edge
            current_edges = edges[:i] + edges[i+1:]
            
            # Build the map without that edge
            m = create_map(current_edges)
            
            # If removing this edge means there is NO cycle left, 
            # then this was the redundant connection!
            if not has_cycle(m):
                return edges[i]

        return []