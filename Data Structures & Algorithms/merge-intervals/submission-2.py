class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        results = []

        def dof(ints):
            previous = None
            for interval in ints:
                if previous:
                    if previous[1] >= interval[0]:
                        previous = [min(previous[0], interval[0]), max(interval[1], previous[1])]
                    else:
                        results.append(previous)
                        previous = None
                if not previous:
                    previous = interval

            if previous:
                results.append(previous)
        
        dof(intervals)

        return results