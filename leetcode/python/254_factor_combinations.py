class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        combos = [[n]]
        for factors in combos:
            n, start = factors[-1], factors[-2] if len(factors) > 1 else 2
            for k in range(start, int(n**0.5) + 1):
                if n % k == 0:
                    combos.append(factors[:-1] + [k, n//k])
        return combos[1:]

s = Solution()
print(s.getFactors(12))