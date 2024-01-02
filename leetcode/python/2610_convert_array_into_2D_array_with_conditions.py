from collections import defaultdict


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if len(res) < count[n]:
                res.append([])
            res[count[n]-1].append(n)
        return res
            
        
        