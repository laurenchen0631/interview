import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        heap: list[int] = []
        stations.append([target, 0])
        tank = startFuel
        prev = res = 0
        for loc, gas in stations:
            tank -= loc - prev
            while heap and tank < 0:
                tank += -heapq.heappop(heap)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(heap, -gas)
            prev = loc
        return res
s = Solution()
print(s.minRefuelStops(target = 1, startFuel = 1, stations = []))
print(s.minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))
print(s.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
        