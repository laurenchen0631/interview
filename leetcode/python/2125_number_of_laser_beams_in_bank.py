class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = res = 0
        for row in bank:
            security = row.count('1')
            if security > 0:
                res += security * prev
                prev = security
        return res
        