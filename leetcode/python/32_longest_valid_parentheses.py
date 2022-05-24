class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s)):
            if s[i] == '(':
                continue
            
            if s[i-1] == '(':
                dp[i+1] = dp[i-1] + 2
            elif i - dp[i] - 1 > -1 and s[i - dp[i] - 1] == '(':
                dp[i+1] = dp[i]+2+dp[i-dp[i]-1]
        return max(dp)

s = Solution()
# print(s.longestValidParentheses('(()'))
# print(s.longestValidParentheses(')()())'))
print(s.longestValidParentheses('()(()())'))
print(s.longestValidParentheses("(()))())("))