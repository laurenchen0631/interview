class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
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

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 7))
    print(s.search([4,5,6,7,0,1,2], 3))
    print(s.search([1], 0))
    print(s.search([5,3,1], 5))