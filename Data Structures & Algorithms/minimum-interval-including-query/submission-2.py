import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        nq = len(queries)
        sq = sorted([i for i in range(nq)], key=lambda x: queries[x])
        intervals.sort(key=lambda x: x[0])

        results = [-1 for i in range(nq)]

        mheap = []
        
        i = iq = 0
        while i < n or iq < nq:
            # Prevent IndexError: if we've answered all queries, we are done
            if iq == nq:
                break
                
            query = queries[sq[iq]]

            # PATH 1: Add intervals that start before or at the current query
            if i < n and intervals[i][0] <= query:
                interval = intervals[i]
                # MUST push the end time so we know when to remove it later
                heapq.heappush(mheap, (interval[1] - interval[0] + 1, interval[1]))
                i += 1  # Advance interval pointer ONLY
            # PATH 2: We have all candidates for this query. Find answer and advance query.
            else:
                # Pop out intervals that ended before this query
                while mheap and mheap[0][1] < query:
                    heapq.heappop(mheap)
                    
                # Check if it fits the query, if yes add to the result
                if mheap:
                    results[sq[iq]] = mheap[0][0]
                    
                iq += 1 # Advance query pointer ONLY

        # Convert the dictionary back to a list in the original query order
        return results