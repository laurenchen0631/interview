from itertools import accumulate


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start: int = -1
        accumul: int = 0
        tank: int = 0
        for i in range(len(gas)):
            t = gas[i] + tank - cost[i]
            if t < 0:
                accumul += t
                start = -1
                tank = 0
            else:
                if start == -1:
                    start = i
                tank = t
        return start if (tank + accumul >= 0) else -1

s = Solution()
print(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(s.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
print(s.canCompleteCircuit(gas = [3,1,1], cost = [1,2,2]))
