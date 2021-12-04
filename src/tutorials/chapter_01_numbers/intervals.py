from typing import List
import heapq


# LC986. Interval List Intersections
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    ret = []
    i = j = 0
    while i < len(firstList) and j < len(secondList):
        left = max(firstList[i][0], secondList[j][0])
        right = min(firstList[i][1], secondList[j][1])
        if left <= right: ret.append((left, right))  # add intersection
        if firstList[i][1] < secondList[j][1]: i += 1  # move short end
        else: j += 1
    return ret


# LC56. Merge Intervals, top100
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]: merged.append(interval)  # no overlap
        else: merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


# LC252. Meeting Rooms
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    si = sorted(intervals)  # sort by first element in asc order
    for i in range(len(si) - 1):
        if si[i][1] > si[i+1][0]: return False
    return True


# LC253. Meeting Rooms II, top100
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals: return 0
    intervals.sort()  # greedy, sort intervals by starting time. O(nlogn)
    rooms = []
    for intv in intervals:
        if rooms and rooms[0] <= intv[0]: # if earliest end time < this start time
            heapq.heappop(rooms) # remove and replace with current end time
        heapq.heappush(rooms, intv[1])  # we sort heap by end time
    return len(rooms)


print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))