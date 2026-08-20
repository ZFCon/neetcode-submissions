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

        # Build the full map once
        m = create_map(edges)

        # Loop through edges in reverse (from last to first)
        for enter, exit in reversed(edges):
            # THE FIX: Temporarily remove this edge from the map so we can test 
            # if a cycle STILL exists using the OTHER edges!
            m[enter].remove(exit)
            m[exit].remove(enter)

            # Check if a cycle still exists without this edge
            if not has_cycle(m):
                return [enter, exit]

            # If it didn't fix the cycle, put the edge back and keep looking
            m[enter].append(exit)
            m[exit].append(enter)

        return []