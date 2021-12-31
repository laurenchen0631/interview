class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([11,13,15,17]))
    print(s.findMin([2, 1]))
    print(s.findMin([3, 1, 2]))
