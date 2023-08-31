from collections import defaultdict
from functools import reduce
from operator import mul


class Solution:
    # group all numbers with the same difference k
    # calculate the number of k-free subsets for each group
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        size = defaultdict(int)
        for n in sorted(nums):
            size[n] = size[n-k] + 1
            size.pop(n-k)
        m = max(size.values())
        fib = [1] * (m+2) # for base case: fib[0] and fib[1]
        # [1, 1, 2, 3, 5, 8]
        # [1] => [], [1]
        # [1,2] => [], [1], [2]
        # [1,2,3] => [], [1], [2], [3], [1,3]
        # [1,2,3,4] k=1 => [], [1], [2], [3], [4], [1,3], [1,4], [2,4]
        for i in range(2, m+2):
            fib[i] = fib[i-2] + fib[i-1]
        return reduce(mul, [fib[v+1] for v in size.values()])