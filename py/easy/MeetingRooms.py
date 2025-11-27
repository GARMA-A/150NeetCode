from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        mx = float("-inf")
        for meeting in intervals :
            start ,end = meeting.start , meeting.end
            if start >= mx:
                mx = end
            else:
                return False

        return True



