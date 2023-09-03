from functools import lru_cache
import heapq
import sys


class Solution:
    def minBuildTime(self, blocks: list[int], split: int) -> int:
        heapq.heapify(blocks)
        while len(blocks) > 1:
            b1 = heapq.heappop(blocks)
            b2 = heapq.heappop(blocks)
            new_block = max(b1, b2) + split
            heapq.heappush(blocks, new_block)
        return blocks[0]
    
    def minBuildTimeDP(self, blocks: list[int], split: int) -> int:
        n = len(blocks)
        blocks.sort(reverse=True)

        @lru_cache(None)
        def solve(i: int, worker: int) -> int:
            if i == n:
                return 0
            elif worker == 0: # not enough worker to finish
                return sys.maxsize
            elif worker >= n - i: # enough workers to do the rest jobs
                return blocks[i]

            working = max(blocks[i], solve(i+1, worker-1))
            spliting = split + solve(i, min(2 * worker, n - i))
            return min(working, spliting)
        return solve(0, 1)