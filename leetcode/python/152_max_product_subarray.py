class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 0:
            raise Exception()
        
        curMax: int = nums[0]
        curMin: int = curMax
        maximum: int = curMax
        for i in range(1, len(nums)):
            n = nums[i]
            (n1, n2) = (curMax * n, curMin * n)
            curMax = max(n, n1, n2)
            curMin = min(n, n1, n2)
            maximum = max(curMax, maximum)

        return maximum

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2, 0, -1]))
    print(s.maxProduct([2,3,-2,4,-6,-20]))