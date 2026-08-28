from collections import defaultdict, deque
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # using dict create a directed graph
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        # sort the destinations alphabetically, then convert to deque
        for src in graph:
            graph[src].sort()
            graph[src] = deque(graph[src])
            
        itinerary = []
        
        # DFS to take all destinations in order
        def dfs(airport):
            # while there are still out-bound flights from this airport
            while graph[airport]:
                # take the first available destination using O(1) popleft
                next_dest = graph[airport].popleft()
                dfs(next_dest)
            
            # append the airport ONLY when it has no more outgoing flights
            itinerary.append(airport)
            
        dfs("JFK")
        
        # Since we appended dead-ends first, the itinerary is backwards. 
        # We reverse it to get the correct chronological flight path.
        return itinerary[::-1]