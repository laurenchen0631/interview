class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            isRightEven = (r - m) % 2 == 0
            if nums[m+1] == nums[m]:
                if isRightEven:
                    l = m + 2
                else:
                    r = m - 1
            elif nums[m-1] == nums[m]:
                if isRightEven:
                    r = m - 2
                else:
                    l = m + 1
            else:
                return nums[m]
            
        return nums[l]
    
s = Solution()
# print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
# print(s.singleNonDuplicate([3,3,7,7,10,11,11]))
print(s.singleNonDuplicate([1,2,2]))