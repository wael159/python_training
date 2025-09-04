def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: sort by start
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]  # Step 2: start with first interval

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        # Step 3: check overlap and merge or append
        if last_end >= start:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


import heapq

def merge_intervals_heap(intervals):
  if not intervals: return []
  heap = [(s, e) for s, e in intervals]
  heapq.heapify(heap)  # O(n)

  s, e = heapq.heappop(heap)
  merged = [[s, e]]

  while heap:
    s, e = heapq.heappop(heap)
    last = merged[-1]
    if s <= last[1]:
      last[1] = max(last[1], e)
    else:
      merged.append([s, e])
  return merged
