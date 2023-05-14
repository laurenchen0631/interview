from math import gcd

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        maxStates = 1 << n
        goal = maxStates - 1
        dp = [0] * maxStates
        for state in range(goal - 1, -1, -1):
            count = bin(state).count('1')
            pairs = count // 2
            if count % 2 == 1:
                continue
            for i in range(n):
                if (state >> i & 1) == 1:
                    continue
                for j in range(i + 1, n):
                    if (state >> j & 1) == 1:
                        continue
                    nextState = state | (1 << i) | (1 << j)
                    score = (pairs + 1) * gcd(nums[i], nums[j])
                    dp[state] = max(dp[state], dp[nextState] + score)
        return dp[0]
