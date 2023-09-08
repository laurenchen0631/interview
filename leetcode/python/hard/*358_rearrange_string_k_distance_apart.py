from typing import Counter


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        n = len(s)
        if not k:
            return s
        
        count = Counter(s)
        
        max_val = max(count.values())
        max_count = sum(1 for val in count.values() if val == max_val)

        # check enough slots, s = "aaabbbcc", k = 3
        # |abc abc|       |ab|
        # (max_val-1)*k   max_count
        if (max_val-1)*k+max_count > n:
            return ""
    
        res = [""] * n
        # We start at i = (n - 1) % k because we want "[jump] from bucket to bucket from left to right BUT each individual bucket being filled
        i = (n-1) % k
        for c in sorted(count, key=lambda c: -count[c]):
            for _ in range(count[c]):
                res[i] = c
                print(res)
                i += k
                if i >= n:
                    print(i)
                    i = (i-1) % k
        return "".join(res)
    
s = Solution()
# print(s.rearrangeString("abcdabcdabdeacb", 4))
print(s.rearrangeString("abcdabcdabdeac", 4))