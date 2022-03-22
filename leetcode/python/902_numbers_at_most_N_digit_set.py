class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        S = str(n)
        k = len(S)
        dp = [0] * (k+1) # dp[i] = total number of valid integers if N was "N[i:]"
        dp[-1] = 1
        
        for i in range(k-1, -1, -1):
            for d in digits:
                if d < S[i]:
                    dp[i] += len(digits) ** (k-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(digits) ** i for i in range(1, k))

s = Solution()
print(s.atMostNGivenDigitSet(digits = ["1","3","5","7"], n = 777))
# print(s.atMostNGivenDigitSet(digits = ["1","4","9"], n = 1000000000))