from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-value, key) for key, value in counter.items()]
        heapify(heap)
        res = []
        while heap:
            count, c = heappop(heap)
            if not res or res[-1] != c:
                res.append(c)
                if count < -1:
                    heappush(heap, (count+1, c))
            else:
                if not heap:
                    return ''
                count2, c2 = heappop(heap)
                res.append(c2)
                if count2 < -1:
                    heappush(heap, (count2+1, c2))
                heappush(heap, (count, c))
        return ''.join(res)