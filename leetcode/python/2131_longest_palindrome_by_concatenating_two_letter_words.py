from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        selfPalindrome: int = 0
        res: int = 0
        counter = Counter(words)
        for w in counter:
            if not counter[w]:
                continue

            if w[0] == w[1]:
                k, r = divmod(counter[w], 2)
                res += 4 * k
                selfPalindrome += r
            elif (p := w[::-1]) in counter:
                res += 4 * min(counter[w], counter[p])
                counter[w] = 0
                counter[p] = 0
                
        return res + 2 if selfPalindrome else res

s = Solution()
print(s.longestPalindrome(["lc","cl","gg"]))
print(s.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
print(s.longestPalindrome(["cc","ll","xx"]))
        