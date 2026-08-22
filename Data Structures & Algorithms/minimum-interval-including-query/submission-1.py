import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        nq = len(queries)
        sq = sorted([i for i in range(nq)], key=lambda x: queries[x])
        intervals.sort(key=lambda x: x[0])

        results = {i: float("inf") for i in range(nq)}

        mheap = []
        
        i = iq = 0
        while i < n or iq < nq:
            # Prevent IndexError: if we've answered all queries, we are done
            if iq == nq:
                break
                
            query = queries[sq[iq]]

            if i < n and intervals[i][0] <= query:
                interval = intervals[i]

                heapq.heappush(mheap, ((interval[1] - interval[0] + 1), interval[1]))
                i += 1
            else:
                while mheap and mheap[0][1] < query:
                    heapq.heappop(mheap)

                if mheap:
                    results[sq[iq]] = mheap[0][0]
                else:
                    results[sq[iq]] = -1

                iq += 1

            


        # Convert the dictionary back to a list in the original query order
        return [results[j] if results[j] != float("inf") else -1 for j in range(nq)]