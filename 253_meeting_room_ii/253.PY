
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        used_room = 0
        end_ptr = 0
        for t in starts:
            if t < ends[end_ptr]:
                used_room += 1
            else:
                end_ptr += 1
        return used_room

# Greedy
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        time.sort(key=lambda x: (x[0], x[1]))
        res = count = 0
        for t, point in time:
            count += point
            res = max(res, count)
        return res