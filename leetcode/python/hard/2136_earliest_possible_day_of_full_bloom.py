class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        orders = sorted(range(len(plantTime)), key=lambda i: growTime[i], reverse=True)
        cur = res = 0
        for i in orders:
            cur += plantTime[i]
            res = max(res, cur + growTime[i])
        return res

s = Solution()
print(s.earliestFullBloom(plantTime = [1,2,3,4,5], growTime = [1,1,1,1,1]))