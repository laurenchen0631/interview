class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        res.append(newInterval)
        return res

s = Solution()
print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(s.insert(intervals = [[1,5]], newInterval = [2,3]))