class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n = len(s)
        if n == 0:
            return []
        last: dict[str, int] = {}
        for i in range(n-1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i
        res: list[int] = []
        prevIndex: int = -1
        lastIndex: int = -1
        for i in range(n):
            if i > lastIndex:
                res.append(last[s[i]] - lastIndex)
                prevIndex = lastIndex
                lastIndex = last[s[i]]
            else:
                res[-1] = max(res[-1], last[s[i]] - prevIndex)
                lastIndex = max(lastIndex, last[s[i]])
        return res

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("eccbbbbdec"))
print(s.partitionLabels("abaccbdeffed"))