class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        dp = [0] * (2 * total + 1)
        dp[nums[0] + total] = 1 ## total works as offset
        dp[-nums[0] + total] += 1
        for i in range(1, len(nums)):
            tmp = [0] * (2 * total + 1)
            for k in range(-total, total+1):
                if (c := dp[k + total]) > 0:
                    tmp[k+nums[i]+total] += c
                    tmp[k-nums[i]+total] += c
            dp = tmp
        return dp[target+total] if abs(target) <= total else 0

s = Solution()
print(s.findTargetSumWays([2,1,1,2], 0))
