from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # 1. Build the full map ONCE at the start
        m = {}
        for i, e in edges:
            m[i] = m.get(i, [])
            m[i].append(e)

            m[e] = m.get(e, [])
            m[e].append(i)

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

            for node in m.keys():
                if node not in visited:
                    if dfs(node, node):
                        return True
            return False

        # 2. Loop through edges in reverse (from last to first)
        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            
            # OPTIMIZATION: If either node is a leaf (only 1 connection), 
            # removing this edge can't possibly break a cycle! Skip the DFS.
            if len(m[u]) == 1 or len(m[v]) == 1:
                continue

            # Temporarily remove the edge in-place (O(1) instead of rebuilding the map)
            m[u].remove(v)
            m[v].remove(u)
            
            # If removing this edge means there is NO cycle left, 
            # then this was the redundant connection!
            if not has_cycle(m):
                return edges[i]
            
            # Put the edge back so the map is intact for the next iteration
            m[u].append(v)
            m[v].append(u)

        return []