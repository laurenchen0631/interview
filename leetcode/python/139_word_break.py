class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set[str](wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[len(s)]

s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))