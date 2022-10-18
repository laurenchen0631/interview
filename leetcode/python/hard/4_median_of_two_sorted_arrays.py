class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m+n) & 1:
            return self.findKth(nums1, nums2, (m+n)//2)
        else:
            return (self.findKth(nums1, nums2, (m+n)//2) + self.findKth(nums1, nums2, (m+n)//2-1)) / 2
    
    def findKth(self, nums1: list[int], nums2: list[int], k: int) -> int:
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        m1, m2 = len(nums1)//2, len(nums2)//2
        if m1 + m2 < k: # need more elements
            if nums1[m1] > nums2[m2]:
                return self.findKth(nums1, nums2[m2+1:], k-m2-1)
            else:
                return self.findKth(nums1[m1+1:], nums2, k-m1-1)
        else:
            if nums1[m1] > nums2[m2]:
                return self.findKth(nums1[:m1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:m2], k)

s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))