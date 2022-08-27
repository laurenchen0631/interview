from math import inf
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -inf
        for l in range(m):
            prefix = [0] * n
            for r in range(l, m):
                for c in range(n):
                    prefix[c] += matrix[r][c]
                res = max(res, self.maxSumSubarray(prefix, k))
        return res

    def maxSumSubarray(self, nums: list[int], k: int) -> int:
        res = -inf
        prefix = 0
        prefixSet = SortedList([0])
        for num in nums:
            prefix += num
            left = self.ceiling(prefixSet, prefix - k)
            if left is not None:
                res = max(res, prefix - left)
            prefixSet.add(prefix)
        return res

    def ceiling(self, nums: SortedList, target: int) -> int:
        i = nums.bisect_left(target)
        return nums[i] if i < len(nums) else None


s = Solution()
print(s.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))