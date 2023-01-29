class Solution:
    def nimGame(self, piles: list[int]) -> bool:
        cache: dict[str, bool] = {}
        def dp(piles: list[int]) -> bool:
            key = '-'.join(map(str, piles))
            if key in cache:
                return cache[key]
            if piles[-1] == 0:
                return False
            for i in range(len(piles)):
                for j in range(1, piles[i] + 1):
                    piles[i] -= j
                    if not dp(sorted(piles)):
                        cache[key] = True
                        return True
                    piles[i] += j
            cache[key] = False
            return False
        return dp(sorted(piles))