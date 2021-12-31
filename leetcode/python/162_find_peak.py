class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l: int = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2,3,1]))
    print(s.findPeakElement([1,2,1,3,5,6,4]))