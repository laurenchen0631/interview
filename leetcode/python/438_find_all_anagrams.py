from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        
        sChars = defaultdict[str, int](int)
        pChars = defaultdict[str, int](int)
        for i in range(len(p)):
            sChars[s[i]] += 1
            pChars[p[i]] += 1

        count: int = 26 # a-z
        for i in range(count):
            c = chr(ord('a') + i)
            if sChars[c] == pChars[c]:
                count -= 1

        res: list[int] = [] if count != 0 else [0]
        i: int = 0
        while i + len(p) < len(s):
            l = s[i]
            r = s[i + len(p)] 
            
            sChars[r] += 1
            if sChars[r] == pChars[r]:
                count -= 1
            elif sChars[r] - pChars[r] == 1:
                count += 1
            
            sChars[l] -= 1
            if sChars[l] == pChars[l]:
                count -= 1
            elif pChars[l] - sChars[l] == 1:
                count += 1

            i += 1
            if count == 0:
                res.append(i)

        return res

    def findAnagramsOpt(self, s: str, p: str) -> list[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))