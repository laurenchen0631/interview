from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = Counter(words)
        heap = [(-counter[s], s) for s in counter.keys()]
        heapq.heapify(heap)
        res: list[str] = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

s = Solution()
print(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
print(s.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))