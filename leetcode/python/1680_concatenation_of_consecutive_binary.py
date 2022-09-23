class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = offset = threshold = 1
        for k in range(2, n+1):
            if k >= threshold:
                offset += 1
                threshold = 2 ** offset
            res = (res << offset) + k
        return res

s = Solution()
print(s.concatenatedBinary(3))
print(s.concatenatedBinary(12))