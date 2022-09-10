class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        n, m = len(target), len(stamp)
        res: list[int] = []
        visited = set[int]()
        cur = list(target)
        for i in range(n - m + 1):
            if not self.matches(stamp, cur[i:i+m]):
                continue

            for j in range(i, -1, -1):
                if j in visited:
                    break
                visited.add(j)
                if self.matches(stamp, cur[j:j+m]):
                    res.append(j)
                    cur[j:j+m] = ['?'] * m
        return res[::-1] if all([c == '?' for c in cur]) else [] 

    def matches(self, s: str, target: list[str]) -> bool:
        for i in range(len(s)):
            if s[i] != target[i] and target[i] != '?':
                return False
        return True

s = Solution()
print(s.movesToStamp(stamp = "abc", target = "ababc"))
print(s.movesToStamp(stamp = "abca", target = "aabcaca"))
print(s.movesToStamp(stamp = "zbs", target = "zbzbsbszbssbzbszbsss"))