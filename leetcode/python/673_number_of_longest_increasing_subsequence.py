class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        longest = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[i] == dp[j] + 1:
                    count[i] += count[j]
            longest = max(longest, dp[i])
        
        res = 0
        for i in range(len(nums)):
            if dp[i] == longest:
                res += count[i]
                    
        return res

s = Solution()
# print(s.findNumberOfLIS([7,7,7,7]))
# print(s.findNumberOfLIS([7]))
# print(s.findNumberOfLIS([1,3,5,4,7]))
# print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))
print(s.findNumberOfLIS([1,2,3,1,2,3,1,2,3]))