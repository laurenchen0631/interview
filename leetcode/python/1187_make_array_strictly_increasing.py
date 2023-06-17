import bisect
from functools import lru_cache

class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        @lru_cache(None)
        def dfs(i: int, prev: int) -> int:
            if i >= len(arr1):
                return 0
            
            cost = len(arr2) + 1
            if arr1[i] > prev:
                cost = dfs(i+1, arr1[i]) # do nothing
            
            j = bisect.bisect_right(arr2, prev)
            if j < len(arr2):
                cost = min(cost, 1 + dfs(i+1, arr2[j]))
            return cost
        v = dfs(0, -1)
        return v if v <= len(arr2) else -1
        