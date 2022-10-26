class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        prev = lower - 1
        res: list[str] = []
        for n in nums + [upper+1]:
            if n - prev > 2:
                res.append(f'{prev+1}->{n-1}')
            elif n - prev == 2:
                res.append(f'{prev+1}')
            prev = n
        return res

s = Solution()
print(s.findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))