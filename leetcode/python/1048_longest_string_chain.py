class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        # for each word let the initial longest chain be 1
        res = {c:1 for c in words}

        for w in words:
            if len(w) > 1:
                for i in range(len(w)):
                    temp = w[:i]+w[i+1:]
                    if temp in res:
                        res[w] = max(res[w], 1+res[temp])
        return max(res.values())

s = Solution()
# print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(s.longestStrChain(["abcd","dbqca"]))
print(s.longestStrChain(["a","ab","ac","bd","abc","abd","abdd"]))