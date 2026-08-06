"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(root: "Node") -> "Node":
            if not root:
                return None

            if root.val in visited:
                return visited[node.val]

            new_node = Node(root.val)
            visited[new_node.val] = new_node
            
            for node in root.neighbors:
                if node.val in visited:
                    subnode = visited[node.val]
                else:
                    subnode = dfs(node)
                new_node.neighbors.append(subnode)

            return new_node
            
        return dfs(node)