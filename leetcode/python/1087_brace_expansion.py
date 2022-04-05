class Solution:
    def expand(self, s: str) -> list[str]:
        return self.combine(self.parse(s))
    
    def parse(self, s: str) -> list[list[str]]:
        option: set[str] | None = None
        parts: list[int] = []
        for c in s:
            if c == '{':
                option = set[str]()
            elif c == '}':
                parts.append(sorted(option))
                option = None
            elif c == ',' and option != None:
                continue
            elif option != None:
                option.add(c)
            else:
                parts.append([c])
        return parts

    def combine(self, parts: list[list[str]]) -> list[str]:
        res: list[str] = []
        n = 1
        for p in parts:
            n *= len(p)
        
        indexes = [0] * len(parts)
        for _ in range(n):
            for i in range(len(parts)-1, -1, -1):
                if indexes[i] < len(parts[i]):
                    break
                else:
                    indexes[i-1] += 1
                    indexes[i] = 0
            chars = []
            for i in range(len(indexes)):
                chars.append(parts[i][indexes[i]])
            res.append(''.join(chars))
            indexes[-1] += 1
        return res


s = Solution()
print(s.expand("{a,b}c{d,e}f"))