class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r-1] == nums[r]:
                r -= 1

            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False

s = Solution()
print(s.search(nums = [2,5,6,0,0,1,2], target = 0))
print(s.search(nums = [2,5,6,0,0,1,2], target = 3))
print(s.search(nums = [3,4,4,3,3,3,3], target = 5))
print(s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))
print(s.search([13,1,1,], 13))
print(s.search([13,1], 1))