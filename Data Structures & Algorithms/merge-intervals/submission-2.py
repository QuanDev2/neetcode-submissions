class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        res = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= res[-1][1]:
                curr_s, curr_e = res.pop()
                res_e = max(curr_e, e)
                res.append([curr_s, res_e])
            else:
                res.append([s, e])
            
        return res