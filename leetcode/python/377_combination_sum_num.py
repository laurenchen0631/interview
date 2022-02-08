class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i-n]
        return dp[-1]

s = Solution()
print(s.combinationSum4([1,2,3], 4))
print(s.combinationSum4([9], 3))
