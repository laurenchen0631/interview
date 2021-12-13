from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Chars = defaultdict[str, int](int)
        s2Chars = defaultdict[str, int](int)
        for i in range(len(s1)):
            s1Chars[s1[i]] += 1
            s2Chars[s2[i]] += 1
        
        count: int = 0
        for i in range(26):
            c = chr(ord('a') + i)
            if s1Chars[c] == s2Chars[c]:
                count += 1

        i = 0
        while count != 26 and i + len(s1) < len(s2):
            l = s2[i]
            r = s2[i + len(s1)]
            
            s2Chars[r] += 1
            if s1Chars[r] == s2Chars[r]:
                count += 1
            elif s2Chars[r] - s1Chars[r] == 1:
                count -= 1

            s2Chars[l] -= 1
            if s1Chars[l] == s2Chars[l]:
                count += 1
            elif s2Chars[l] - s1Chars[l] == -1:
                count -= 1
            i += 1
        
        return count == 26

if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))
    print(s.checkInclusion("hello", "ooolleoooleh"))
    print(s.checkInclusion("abc", "bbbca"))
    print(s.checkInclusion("rokx", "otrxvfszxroxrzdsltg"))

    
