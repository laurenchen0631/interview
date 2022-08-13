from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        k = len(words[0])
        counter = Counter(words)
        res: list[int] = []

        def helper(l: int) -> None:
            found = defaultdict(int)
            used: int = 0
            excess: bool = False
            for r in range(l, len(s), k):
                if r + k > len(s):
                    break

                sub = s[r:r+k]
                if sub not in counter:
                    found = defaultdict(int)
                    used = 0
                    excess = False
                    l = r + k
                    continue
                
                while r - l == k * len(words) or excess:
                    lsub = s[l:l+k]
                    l += k
                    found[lsub] -= 1
                    if found[lsub] == counter[lsub]:
                        excess = False
                    else:
                        used -= 1
                
                found[sub] += 1
                if found[sub] <= counter[sub]:
                    used += 1
                else:
                    excess = True
                
                if used == len(words) and not excess:
                    res.append(l)
            
        for i in range(k):
            helper(i)
        return res

s = Solution()
# print(s.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
# print(s.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(s.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))