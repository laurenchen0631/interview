class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        posCount = negCount = preCount = postCount = 0
        res: int = 0
        for n in nums + [0]:
            if n == 0:
                if negCount & 1 == 0:
                    res = max(res, posCount + negCount)
                else:
                    res = max(res, posCount - min(preCount, postCount) + (negCount - 1))
                posCount = negCount = preCount = posCount = 0
            elif n < 0:
                negCount += 1
                postCount = 0
            else:
                if negCount == 0:
                    preCount += 1
                else:
                    postCount += 1
                posCount += 1
        return res

s = Solution()
print(s.getMaxLen([1,-2,-3,4]))
print(s.getMaxLen([0,1,-2,-3,-4]))
print(s.getMaxLen([-1,-2,-3,0,1]))
print(s.getMaxLen([0,0,0,1]))
            