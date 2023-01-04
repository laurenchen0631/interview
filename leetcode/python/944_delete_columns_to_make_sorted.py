class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        if len(strs) < 2:
            return 0
        res: int = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j - 1][i]:
                    res += 1
                    break
        return res