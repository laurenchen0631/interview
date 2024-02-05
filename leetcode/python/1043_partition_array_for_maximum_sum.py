class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n: int = len(arr)
        dp: list[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val: int = 0
            for j in range(1, min(k, i) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
        return dp[n]