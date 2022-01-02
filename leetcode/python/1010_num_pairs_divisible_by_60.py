class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        timeMap: dict[int, int] = {}
        for i in range(len(time)):
            time[i] = time[i] % 60
            timeMap[time[i]] = timeMap.get(time[i], 0) + 1
        
        pairs: int = 0
        for t in time:
            timeMap[t] -= 1
            if (t2 := (60 - t) % 60) in timeMap:
                pairs += timeMap[t2]
        return pairs

    def numPairsDivisibleBy60Opt(self, time: list[int]) -> int:
        timeMap: dict[int, int] = {}
        pairs: int = 0
        for t in time:
            t = t % 60
            if (t2 := (60 - t) % 60) in timeMap:
                pairs += timeMap[t2]
            timeMap[t] = timeMap.get(t, 0) + 1
        return pairs
            

if __name__ == '__main__':
    s = Solution()
    print(s.numPairsDivisibleBy60Opt([30,20,150,100,40]))
    print(s.numPairsDivisibleBy60Opt([60,60,60]))