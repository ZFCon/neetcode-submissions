from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        results = []
        inserted = False

        i = 0
        while i < n:
            # Condition 1: New interval ends before the current interval starts
            if newInterval[1] < intervals[i][0]:
                results.append(newInterval)
                inserted = True
                results.extend(intervals[i:])  # Append remaining intervals
                break
            
            # Condition 2: They conflict/overlap -> Merge using min and max without inserting yet
            elif newInterval[0] <= intervals[i][1]:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
            
            # Condition 3: Current interval comes strictly before new interval -> Append current
            else:
                results.append(intervals[i])
                
            i += 1

        # If newInterval was not inserted during the loop, append it at the end
        if not inserted:
            results.append(newInterval)

        return results