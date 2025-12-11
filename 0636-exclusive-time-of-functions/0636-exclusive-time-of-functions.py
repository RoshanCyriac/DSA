class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n          # exclusive time for each function
        stack = []             # call stack: stores function ids
        prev_time = 0          # last processed timestamp

        for log in logs:
            fid_str, typ, time_str = log.split(":")
            fid = int(fid_str)
            time = int(time_str)

            if typ == "start":
                # previous function (if any) ran from prev_time to time - 1
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:  # "end"
                # current function ends at 'time' inclusive
                stack.pop()
                res[fid] += time - prev_time + 1
                prev_time = time + 1

        return res
