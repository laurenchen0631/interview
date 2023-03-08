class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        l = 0
        r = max(time) * totalTrips
        while l < r:
            m = (l + r) // 2
            trips = sum([m // t for t in time])
            if trips >= totalTrips:
                r = m
            else:
                l = m + 1
        return l
    
s = Solution()
print(s.minimumTime([1,3,2], 5))