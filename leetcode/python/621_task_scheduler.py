from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        freq.sort()

        fMax = freq.pop()
        idleTime = (fMax - 1) * n
        while freq and idleTime > 0:
            f = freq.pop()
            if not f:
                break
            idleTime -= min(fMax - 1, f)
        return len(tasks) + max(0, idleTime)

s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
