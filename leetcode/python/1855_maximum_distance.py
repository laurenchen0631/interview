class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i = j = 0
        dist = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                dist = max(dist, j - i)
                j += 1
        return dist

s = Solution()
print(s.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
print(s.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
print(s.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))