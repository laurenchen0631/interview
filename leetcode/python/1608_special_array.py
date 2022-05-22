class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        l = 0
        r = len(nums)
        while l < r:
            m = (l+r) // 2
            if m < nums[m]:
                l = m + 1
            else:
                r = m
        return -1 if l < len(nums) and l == nums[l] else l

s = Solution()
print(s.specialArray([3,5]))
print(s.specialArray([1,1,2]))
print(s.specialArray([0,4,3,0,4]))
