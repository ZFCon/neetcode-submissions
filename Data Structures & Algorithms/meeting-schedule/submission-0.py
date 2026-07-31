"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)

        previous = None
        for interval in intervals:
            if previous and previous.end > interval.start:
                return False

            previous = interval

        return True