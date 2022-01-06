class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        stops = [0] * 1001
        firstStop = lastStop = 0
        for [n, start, end] in trips:
            stops[start] += n
            stops[end] -= n
            lastStop = max(lastStop, end)
            firstStop = min(firstStop, start)
        
        for i in range(firstStop, lastStop):
            stops[i] += stops[i-1]
            if stops[i] > capacity:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.carPooling([[2,1,5],[3,3,7]], 4))
    print(s.carPooling([[2,1,5],[3,3,7]], 5))
    print(s.carPooling([[9,0,1],[3,3,7]], 4))