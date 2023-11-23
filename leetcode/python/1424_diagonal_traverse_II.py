from collections import defaultdict


class Solution:
    # (0,0), (1,0), (0,1), (2,0), (1,1), (0,2), (2,1), (1,2), (2,2)
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        groups = defaultdict(list[int])
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])):
                diagonal = i + j
                groups[diagonal].append(nums[i][j])
        
        res = []
        for i in range(len(groups.keys())):
            res.extend(groups[i])
        return res