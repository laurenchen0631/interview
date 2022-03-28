from typing import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if not nums1 or not nums2:
            return []
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        count = Counter(nums2)
        res: list[int] = []
        for n in nums1:
            if n in count and count[n] > 0:
                count[n] -= 1
                res.append(n)
        return res

s = Solution()
print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
