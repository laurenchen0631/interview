class Solution:
    def findPermutation(self, s: str) -> list[int]:
        perm = list(range(1, len(s) + 2))
        i: int = 0
        while i < len(s):
            while i < len(s) and s[i] == 'I':
                i += 1
            l = i
            while i < len(s) and s[i] == 'D':
                i += 1
            r = i
            while l < r:
                perm[l], perm[r] = perm[r], perm[l]
                l += 1
                r -= 1
        return perm

s = Solution()
print(s.findPermutation('IDI'))
print(s.findPermutation('DDD'))
print(s.findPermutation('DDI'))
print(s.findPermutation('DDID'))