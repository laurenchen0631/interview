class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        rotated = 0
        cur = n
        while cur > 0:
            cur, digit = divmod(cur, 10)
            if digit not in mapping:
                return False
            rotated = rotated * 10 + mapping[digit]
        return rotated != n