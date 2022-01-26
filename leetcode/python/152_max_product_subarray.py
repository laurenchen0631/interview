class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curMax = curMin = maximum = nums[0]
        for n in nums[1:]:
            curMax *= n 
            curMin *= n 
            curMax, curMin = max(n, curMax, curMin), min(n, curMax, curMin)
            maximum = max(maximum, curMax)

        return maximum

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2, 0, -1]))
    print(s.maxProduct([2,3,-2,4,-6,-20]))