class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(
            self.robImpl(nums[:-1]),
            self.robImpl(nums[1:])
        )
    
    def robImpl(self, nums: list[int]) -> int:
        t1: int = 0 # steal
        t2: int = 0 # skip
        for n in nums:
            t1, t2 = max(t2+n, t1), t1
        return t1

if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))
    print(s.rob([1,2,3]))