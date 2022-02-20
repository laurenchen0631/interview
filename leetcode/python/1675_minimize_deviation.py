from cmath import inf
import heapq

class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        evens: list[int] = []
        minimum = inf
        for n in nums:
            if n & 1 == 1:
                evens.append(-n*2)
            else:
                evens.append(-n)
            minimum = min(minimum, -evens[-1])
        heapq.heapify(evens)
        res: int = inf
        while evens:
            v = -heapq.heappop(evens)
            res = min(res, v - minimum)
            if v & 1 == 0:
                minimum = min(minimum, v // 2)
                heapq.heappush(evens, -v // 2)
            else: ## odd max can't get smaller
                break
        return res
        

s = Solution()
print(s.minimumDeviation([1,2,3,4]))
print(s.minimumDeviation([4,1,5,20,3]))
print(s.minimumDeviation([2,10,8]))