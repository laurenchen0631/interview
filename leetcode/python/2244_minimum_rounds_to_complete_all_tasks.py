from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        difficulty = Counter(tasks)
        res = 0
        for v in difficulty.values():
            if v == 1:
                return -1
            k, r = divmod(v, 3)
            if r == 1:
                res += k + 1
            else:
                res += k + r // 2
        return res

s = Solution()
print(s.minimumRounds([2,2,3,3,2,4,4,4,4,4]))