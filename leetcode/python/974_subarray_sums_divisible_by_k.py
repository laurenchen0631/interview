from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
            prefix = res = 0
            count = defaultdict(int)
            count[0] = 1
            for n in nums:
                prefix = (prefix + n) % k
                res += count[prefix]
                count[prefix] += 1
            return res

