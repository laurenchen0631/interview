from math import ceil, log2

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        state = minutesToTest // minutesToDie + 1
        return ceil(log2(buckets) / log2(state))