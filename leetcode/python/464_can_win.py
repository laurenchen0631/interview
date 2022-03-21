class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        maxTotal = (maxChoosableInteger+1) * maxChoosableInteger / 2
        if maxTotal < desiredTotal:
            return False
        elif maxTotal == desiredTotal:
            return maxChoosableInteger & 1 == 1

        cache: dict[tuple, bool] = {}
        def dp(choices: list[int], remain: int) -> bool:
            if choices[-1] >= remain:
                return True
            key = tuple(choices)
            if key in cache:
                return cache[key]

            cache[key] = False
            for i in range(len(choices)):
                if not dp(choices[:i] + choices[i+1:], remain - choices[i]):
                    cache[key] = True
                    break
            return cache[key]
        return dp([i for i in range(1, maxChoosableInteger+1)], desiredTotal)

s = Solution()
print(s.canIWin(maxChoosableInteger = 10, desiredTotal = 11))
print(s.canIWin(maxChoosableInteger = 10, desiredTotal = 1))
print(s.canIWin(18, 79))
