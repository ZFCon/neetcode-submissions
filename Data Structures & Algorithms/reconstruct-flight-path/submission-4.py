from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: (x[0], x[1]))
        # using dict create a directed graph
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        itinerary = []
        
        # DFS to take all destinations in order
        def dfs(airport):
            # while there are still out-bound flights from this airport
            while graph[airport]:
                # take the first available destination
                next_dest = graph[airport].pop(0)
                dfs(next_dest)
            
            # append the airport ONLY when it has no more outgoing flights
            itinerary.append(airport)
            
        dfs("JFK")
        
        # Since we appended dead-ends first, the itinerary is backwards. 
        # We reverse it to get the correct chronological flight path.
        return itinerary[::-1]