class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in t:
            cnt[ord(c) - ord('a')] -= 1
        return sum([abs(x) for x in cnt]) // 2