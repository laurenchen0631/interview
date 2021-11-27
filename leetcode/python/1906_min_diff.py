class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        maxDiff = max(nums) - min(nums)
        diffs = self._helper(nums, maxDiff)
        res: list[int] = []
        for q in queries:
            [l, r] = q
            minVal = min(diffs[l][:r-l])
            for i in range(l+1, r):
                minVal = min(diffs[i][:r-i] + [minVal])
            res.append(minVal if minVal <= maxDiff else -1)
        return res

    def _helper(self, nums: list[int], maxVal: int) -> dict[int, list[int]]:
        diffs: map[int, list[int]] = {}
        for i in range(len(nums) - 1):
            diffs[i] = []
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    diffs[i].append(maxVal + 1)
                else:
                    diffs[i].append(abs(nums[i] - nums[j]))
        return diffs

if __name__ == '__main__':
    s = Solution()
    print(s.minDifference([1,3,4,8], [[0,1],[1,2],[2,3],[0,3]]))
    print(s.minDifference([4,5,2,2,7,10], [[2,3],[0,2],[0,5],[3,5]]))