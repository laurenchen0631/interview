from re import X


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[0].append([])
        words = set(wordDict)
        for i in range(1, len(s) + 1):
            for w in words:
                if len(w) > i or s[i-len(w):i] != w:
                    continue
                
                for sub in dp[i-len(w)]:
                    dp[i].append(sub + [w])
        return [' '.join(w) for w in dp[-1]]

s = Solution()
print(s.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
print(s.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))