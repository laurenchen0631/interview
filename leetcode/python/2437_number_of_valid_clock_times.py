class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if time[0] == '?' and time[1] == '?':
            res *= 24
        elif time[0] == '?' and time[1] != '?':
            res *= 3 if time[1] <= '3' else 2
        elif time[0] != '?' and time[1] == '?':
            res *= 4 if time[0] == '2' else 10
        
        if time[3] == '?':
            res *= 6
        if time[4] == '?':
            res *= 10
        return res


s = Solution()
print(s.countTime("0?:0?"))
print(s.countTime("?5:00"))
print(s.countTime("?5:??"))
print(s.countTime("??:??"))
print(s.countTime("12:??"))
print(s.countTime("12:?0"))
print(s.countTime("2?:?0"))
print(s.countTime("2?:??"))
print(s.countTime("?4:22"))