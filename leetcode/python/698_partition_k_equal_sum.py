class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        target, r = divmod(total, k)
        if r != 0:
            return False
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            for i in range(n):
                if mask & (1 << i) == 0 and (v := dp[mask] + nums[i]) <= target:
                    dp[mask | (1 << i)] = v % target
                if dp[-1] == 0:
                    return True
            
        return dp[-1] == 0

s = Solution()
print(s.canPartitionKSubsets([4,3,2,3,5,2,1], k = 4))
print(s.canPartitionKSubsets([1,2,3,4,5], k = 5))