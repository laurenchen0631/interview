class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        existed = set([int(k, 2) for k in nums])
        for i in range(2 ** n):
            if i not in existed:
                return format(i, f"0{n}b")
        return ""
        