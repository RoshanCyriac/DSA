class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        merge_intervals = [intervals[0]]
        for start, end in intervals[1:]:
            last_interval = merge_intervals[-1][1]
            if last_interval < start:
                merge_intervals.append([start, end])
            else:
                merge_intervals[-1][1] = max(last_interval , end)
        return merge_intervals