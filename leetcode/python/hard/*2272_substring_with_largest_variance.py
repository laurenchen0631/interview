from collections import Counter


class Solution:
    def largestVariance(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for c1, _ in count.items():
            for c2, rest in count.items():
                if c1 == c2:
                    continue
                
                c1Count = c2Count = 0
                for c in s:
                    if c == c1:
                        c1Count += 1
                    elif c == c2:
                        c2Count += 1
                        rest -= 1
                    
                    if c2Count > 0:
                        res = max(res, c1Count - c2Count)
                        
                    if c2Count > c1Count and rest > 0:
                        c1Count = 0
                        c2Count = 0
                
        return res