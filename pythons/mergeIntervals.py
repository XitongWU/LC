class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=(lambda x:x[0]))
        res_lst = [intervals[0]]
        j = 0
        for i in range(1, len(intervals)):
            if res_lst[j][1] >= intervals[i][0]:
                res_lst[j][1] = max(intervals[i][1],res_lst[j][1])
            else:
                res_lst.append(intervals[i])
                j += 1
                
        return res_lst
        
    def insert(intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

sol = Solution()
interv = [[1,3],[2,6],[8,10],[15,18]]
interv = [[1,4],[4,5]]
print(sol.merge(intervals=interv))

