class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        res = 0
        for k in left:
            res = max(res, k)
        for k in right:
            res = max(res, n - k)
        return res