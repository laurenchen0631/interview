import itertools


class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(n)]
        accSum = [0] + list(itertools.accumulate(nums))
        
        for k in range(1, m + 1):
            for i in range(n):
                if k == 1:
                    dp[i][k] = accSum[n] - accSum[i]
                    continue

                # Determine the minimum largest subarray sum between i and n with k subarrays remaining.
                minimum = accSum[n]
                for j in range(i, n - k + 1):
                    # Store the sum of the first subarray.
                    first_split_sum = accSum[j + 1] - accSum[i]

                    # Find the maximum subarray sum for the current first split.
                    minimum = min(minimum, max(first_split_sum, dp[j + 1][k - 1]))

                    if first_split_sum >= minimum:
                        break
            
                dp[i][k] = minimum
        
        
        return dp[0][m]

s = Solution()
print(s.splitArray(nums = [7,2,5,10,8], m = 2))
# print(s.splitArray(nums = [1,2,3,4,5], m = 2))