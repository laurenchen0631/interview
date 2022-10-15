from functools import lru_cache
import sys


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @lru_cache(None)
        def dp(i: int, k: int, compressed: str, compressCount: int) -> int:
            if k < 0:
                return sys.maxsize
            if i == n:
                return 0
            
            deleteState = dp(i + 1, k - 1, compressed, compressCount)
            keepState = dp(i + 1, k, s[i], 1) + 1 if s[i] != compressed else dp(i + 1, k, compressed, compressCount + 1) + (compressCount in [1, 9, 99])
            return min(deleteState, keepState)
        return dp(0, k, '', 0)
                
s = Solution()
print(s.getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
print(s.getLengthOfOptimalCompression(s = "aabbaa", k = 2))
print(s.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0))
print(s.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 2))
