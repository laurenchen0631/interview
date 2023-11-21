class Solution:
    # [42, 79] -> [24, 97]
    # 42 + 97 = 139, 79 + 24 = 103
    # [13, 10, 35, 24, 76] -> [31, 1, 53, 42, 67]
    # 18: 3, -9: 2
    # 3 * 2 / 2 + 2 * 1 / 2
    def countNicePairs(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        rev_diff = dict[int,int]()
        for n in nums:
            diff = self.rev(n) - n
            rev_diff[diff] = rev_diff.get(diff, 0) + 1
        res = 0
        for _, v in rev_diff.items():
            if v > 1:
                res = (res + v * (v-1) // 2) % MOD
        return res
    
    def rev(self, num: int) -> int:
        res = 0
        while num:
            num, d = divmod(num, 10)
            res = res * 10 + d
        return res
        