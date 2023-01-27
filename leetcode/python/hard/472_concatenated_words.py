
class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        wordSet = set(words)
        res: list[str] = []
        def dfs(i: int, s: str) -> bool:
            if i == len(s):
                res.append(s)
                return True
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and dfs(j, s):
                    return True
            return False
        for s in words:
            wordSet.remove(s)
            dfs(0, s)
            wordSet.add(s)
        return res
    
s = Solution()
print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))