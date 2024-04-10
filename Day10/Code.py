class Solution:
  def insert(self, intervals, newInterval):
    n = len(intervals)
    res = []
    i =0
     
    while (i<n) and (intervals[i].end<newInterval.start):
      res.append(intervals[i])
      i+=1
       
    while (i<n) and (intervals[i].start<=newInterval.end):
      newInterval.start = min(intervals[i].start,newInterval.start)
      newInterval.end = max(intervals[i].end,newInterval.end)
      i+=1
       
    res.append(newInterval)
     
    while i<n :
      res.append(intervals[i])
      i+=1
     
    return res