class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set[str]()
        for i in range(len(s)-k+1):
            codes.add(s[i:i+k])
            if len(codes) == 2 ** k:
                return True
        return False

s = Solution()
# print(s.hasAllCodes(s = "00110110", k = 2))
# print(s.hasAllCodes(s = "0110", k = 1))
# print(s.hasAllCodes(s = "0110", k = 2))
print(s.hasAllCodes(s = "00110", k = 2))