from collections import defaultdict
from email.policy import default


class Solution:
    def anagramMappings(self, nums1: list[int],  nums2: list[int]) -> list[int]:
        index = defaultdict(list[int])
        for i, n in enumerate(nums2):
            index[n].append(i)
        return [index[n].pop() for n in nums1]