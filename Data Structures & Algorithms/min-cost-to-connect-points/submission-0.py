import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
            
        # create dict with directed nodes
        graph = {}
        
        for point1 in points:
            # so the node is a point 
            node = tuple(point1)
            graph[node] = []
            
            # and each node has a list of all the nodes in the points
            for point2 in points:
                # it should have the distance as well in the dict
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                target_node = tuple(point2)
                
                graph[node].append((distance, target_node))
                
        # create a visited set
        visited = set()
        
        # min heap
        min_heap = []
        
        total_cost = 0
        first_node = tuple(points[0])
        visited.add(first_node)
        
        # and dfs
        def dfs(current_node):
            nonlocal total_cost
            
            if len(visited) == len(points):
                return
                
            # before going into the append process make sure you clear up any visited edge from the top of the heap
            while min_heap and min_heap[0][1] in visited:
                heapq.heappop(min_heap)
                
            # append all the connected nodes to the heap and sort them by distance (heapq handles sorting)
            for dist, target_node in graph[current_node]:
                if target_node not in visited:
                    heapq.heappush(min_heap, (dist, target_node))
                    
            # make sure the absolute smallest one we are about to pop is also not visited
            while min_heap and min_heap[0][1] in visited:
                heapq.heappop(min_heap)
                
            if min_heap:
                # after that take the smallest one and add it to visited
                cost, next_node = heapq.heappop(min_heap)
                visited.add(next_node)
                total_cost += cost
                
                # after choosing each edge you go to next node and repeat the process
                dfs(next_node)
                
        # the dfs start from the first node
        dfs(first_node)
        
        return total_cost