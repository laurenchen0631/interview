class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        prev = 0
        for i in range(n):
            if i % 7 == 0:
                prev = i // 7
            prev += 1
            res += prev
        return res