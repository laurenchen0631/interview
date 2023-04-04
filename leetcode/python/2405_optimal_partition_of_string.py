
class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        lastSeen = [-1] * 26
        l = 0
        for i, c in enumerate(s):
            if lastSeen[ord(c) - ord('a')] >= l:
                count += 1
                l = i
            lastSeen[ord(c) - ord('a')] = i
        return count